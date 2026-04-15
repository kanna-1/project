#!/usr/bin/env python3
"""Fetch YouTube metadata plus transcript and save as markdown."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi
from yt_dlp import YoutubeDL


def fetch_metadata(url: str) -> dict:
    with YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
        return ydl.extract_info(url, download=False)


def fetch_transcript(video_id: str) -> str:
    transcript = YouTubeTranscriptApi().fetch(video_id, languages=["en"])
    return "\n".join(segment.text.strip() for segment in transcript if segment.text.strip())


def build_markdown(metadata: dict, transcript_text: str) -> str:
    cleaned = {
        "title": metadata.get("title", ""),
        "channel": metadata.get("channel", ""),
        "upload_date": metadata.get("upload_date", ""),
        "duration": metadata.get("duration", 0),
        "webpage_url": metadata.get("webpage_url", ""),
        "id": metadata.get("id", ""),
    }
    return (
        f"# {cleaned['title']}\n\n"
        f"```json\n{json.dumps(cleaned, indent=2, ensure_ascii=True)}\n```\n\n"
        "## Transcript\n\n"
        f"{transcript_text}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("output", help="Output markdown path")
    args = parser.parse_args()

    metadata = fetch_metadata(args.url)
    transcript_text = fetch_transcript(metadata["id"])

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_markdown(metadata, transcript_text), encoding="utf-8")


if __name__ == "__main__":
    main()
