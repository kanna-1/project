#!/usr/bin/env python3
"""Fetch a public LinkedIn post and save it as markdown."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

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
    value = json.loads(f'"{raw}"')
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


def fetch_post(url: str) -> dict[str, str]:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    response.raise_for_status()
    page = response.text

    social_title_match = re.search(
        r'<meta name="twitter:title" content="(.*?)\|\s*([^|]+?)\s*(?:\|\s*\d+\scomments|posted on the topic\s*\|\s*LinkedIn)">',
        page,
        re.DOTALL,
    )
    if social_title_match:
        title_blob = html.unescape(social_title_match.group(1)).strip()
        headline = re.split(r"\n\s*\n|\n", title_blob, maxsplit=1)[0].strip()
        author = html.unescape(social_title_match.group(2).strip())
    else:
        headline = extract_json_value(page, "headline") or "Untitled LinkedIn post"
        author = ""
    article_body = extract_json_value(page, "articleBody") or ""
    published = extract_json_value(page, "datePublished") or ""

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
    parser.add_argument("url", help="Public LinkedIn post URL")
    parser.add_argument("output", help="Output markdown path")
    args = parser.parse_args()

    post = fetch_post(args.url)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_markdown(post), encoding="utf-8")


if __name__ == "__main__":
    main()
