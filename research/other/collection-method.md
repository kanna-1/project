# Collection Method

## Goal

Build a reusable research corpus for `LinkedIn organic content strategy for B2B SaaS`, with enough signal to turn into a later playbook.

## Workflow

1. Identify practitioners with clear B2B SaaS operating context.
2. Validate that they publish recent public content on LinkedIn and/or YouTube.
3. Save public LinkedIn posts as markdown with metadata.
4. Save YouTube video metadata plus transcript text as markdown.
5. Summarize expert quality and rationale in `research/sources.md`.

## Tools Used

- `requests` for public LinkedIn post fetches
- `yt-dlp` for YouTube metadata
- `youtube-transcript-api` for transcript extraction
- two helper scripts in `scripts/`

## Commands

```bash
python3 scripts/fetch_linkedin_post.py "<public-linkedin-post-url>" "<output-file>.md"
python3 scripts/fetch_youtube_transcript.py "<youtube-video-url>" "<output-file>.md"
```

## Notes

- LinkedIn collection was limited to public post pages available without login.
- YouTube transcripts were collected from available English transcripts.
- I prioritized higher-signal operator content over maximizing file count.
