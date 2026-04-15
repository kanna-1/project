#!/usr/bin/env python3
"""Fetch a public LinkedIn post and save it as markdown.

This script does not discover posts on its own. You must manually supply a
public LinkedIn post URL, then the script fetches that page and extracts the
metadata and body text.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from json import JSONDecodeError

import requests


USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
)


def extract_json_value(page: str, key: str) -> str | None:
    patterns = {
        "headline": r'"headline":"(.*?)","author"',
        "articleBody": r'"articleBody":"(.*?)","author":',
        "datePublished": r'"datePublished":"(.*?)"',
    }
    match = re.search(patterns.get(key, rf'"{re.escape(key)}":"(.*?)"'), page, re.DOTALL)
    if not match:
        return None
    raw = match.group(1)
    try:
        value = json.loads(f'"{raw}"')
    except JSONDecodeError:
        value = raw.split('","', 1)[0]
        value = bytes(value, "utf-8").decode("unicode_escape", errors="ignore")
    if any(token in value for token in ("â", "Ã", "\x80", "\x99")):
        try:
            value = value.encode("latin1").decode("utf-8")
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return value


def normalize_body(text: str) -> str:
    text = text.replace("\\n", "\n")
    text = html.unescape(text)
    text = text.replace("\r\n", "\n").strip()
    return text


def pick_title(candidate: str | None, fallback: str | None) -> str:
    title = (candidate or "").strip()
    if not title or title.lower() in {"text", "image", "video", "link"}:
        title = (fallback or "").strip()
    return title or "Untitled LinkedIn post"


def fetch_post(url: str) -> dict[str, str]:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    page = response.text

    social_title_match = re.search(
        r'<meta name="twitter:title" content="(.*?)\|\s*([^|]+?)\s*(?:(?:\|\s*\d+\scomments)|(?:posted on the topic\s*\|\s*LinkedIn)|(?:\|\s*LinkedIn)|(?:\">))',
        page,
        re.DOTALL,
    )
    if social_title_match:
        title_blob = html.unescape(social_title_match.group(1)).strip()
        social_headline = re.split(r"\n\s*\n|\n", title_blob, maxsplit=1)[0].strip()
        author = html.unescape(social_title_match.group(2).strip())
    else:
        social_headline = ""
        author = ""
    json_headline = extract_json_value(page, "headline") or ""
    article_body = extract_json_value(page, "articleBody") or ""
    published = extract_json_value(page, "datePublished") or ""
    headline = pick_title(social_headline, json_headline or article_body.splitlines()[0] if article_body else "")

    return {
        "author": author,
        "headline": html.unescape(headline),
        "published": published,
        "body": normalize_body(article_body),
        "url": url,
    }


def build_markdown(post: dict[str, str]) -> str:
    metadata = {
        "author": post["author"],
        "title": post["headline"],
        "published_at": post["published"],
        "source_url": post["url"],
    }
    frontmatter = json.dumps(metadata, indent=2, ensure_ascii=True)
    return (
        f"# {post['headline']}\n\n"
        f"```json\n{frontmatter}\n```\n\n"
        f"{post['body']}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Public LinkedIn post URL collected manually")
    parser.add_argument("output", help="Output markdown path")
    args = parser.parse_args()

    post = fetch_post(args.url)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_markdown(post), encoding="utf-8")


if __name__ == "__main__":
    main()
