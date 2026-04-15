# Collection Method

## Goal

Build a reusable research corpus for `LinkedIn organic content strategy for B2B SaaS`, with enough signal to turn into a later playbook.

## Workflow

1. Identify practitioners with clear B2B SaaS operating context.
2. Validate that they publish recent public content on LinkedIn and/or YouTube.
3. Manually collect a public LinkedIn post URL for each expert.
4. Pass each LinkedIn URL into `scripts/fetch_linkedin_post.py`.
5. Save YouTube video metadata plus transcript text as markdown.
6. Summarize expert quality and rationale in `research/sources.md`.

## Tools Used

- `requests` for public LinkedIn post fetches
- `yt-dlp` for YouTube metadata
- `youtube-transcript-api` for transcript extraction
- two helper scripts in `scripts/`

## Commands

```bash
# LinkedIn requires a manually supplied public post URL
python3 scripts/fetch_linkedin_post.py "<public-linkedin-post-url>" "<output-file>.md"

# YouTube can be fetched directly from a public video URL
python3 scripts/fetch_youtube_transcript.py "<youtube-video-url>" "<output-file>.md"
```

## Notes
- The LinkedIn script does not discover posts automatically; it only fetches a post after a public URL is supplied.
- For this repo, the latest LinkedIn posts were refreshed from manually provided public URLs.
- For this repo, selected YouTube transcript files were also refreshed from manually provided public video URLs.
- YouTube transcripts were collected from available English transcripts.
- I prioritized higher-signal operator content over maximizing file count.
