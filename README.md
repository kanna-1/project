# project

## Research Project

This repository now contains a research project on `LinkedIn organic content strategy for B2B SaaS`.

I chose this topic because it sits at the center of modern B2B SaaS growth:
- it helps companies build awareness with the right buyers
- it compounds trust before a buyer is ready to talk to sales
- it can directly influence demos, pipeline, and category positioning
- it leaves behind a strong public trail of real operator content to study

## Why These Experts

I prioritized practitioners who actually operate in B2B SaaS growth, founder-led marketing, content distribution, or social selling. The goal was to avoid generic “LinkedIn gurus” and instead collect material from people who tie content to:
- inbound pipeline
- founder-led demand generation
- zero-click strategy
- personal brand systems
- distribution and amplification
- sales outcomes

The current corpus includes:
- `10` primary experts
- `12` LinkedIn post captures organized by author
- `8` YouTube transcript files captured programmatically
- `1` supplemental interview source

The full expert list, links, dates, and annotations are in [research/sources.md](research/sources.md).

## Repository Layout

```text
research/
├── sources.md
├── linkedin-posts/
├── youtube-transcripts/
└── other/
scripts/
├── fetch_linkedin_post.py
└── fetch_youtube_transcript.py
```

## Collection Workflow

I used lightweight scripts so the process is repeatable rather than manual-only:
- `scripts/fetch_linkedin_post.py` saves public LinkedIn posts into markdown with metadata
- `scripts/fetch_youtube_transcript.py` saves YouTube metadata plus transcript text

Method notes and commands are documented in [research/other/collection-method.md](research/other/collection-method.md).

## Tools installed

| Tool | Purpose |
|------|---------|
| **Cursor** | IDE for this repository |
| **Claude Code** (Cursor extension) | AI-assisted coding inside the editor |
| **Codex** (Cursor extension) | Additional AI coding assistance in the IDE |

## Steps completed

1. Installed **Cursor IDE**.
2. Installed the **Claude Code** and **Codex** extensions in Cursor.
3. Opened the existing GitHub account: [https://github.com/kanna-1/](https://github.com/kanna-1/).
4. Created a new GitHub repository named **`project`** under that account.
5. Created a local folder **`project`** and opened it in Cursor.
6. Initialized Git and linked the folder to the remote, then pushed the first commit:

   ```bash
   echo "# project" >> README.md
   git init
   git add README.md
   git commit -m "first commit"
   git branch -M main
   git remote add origin https://github.com/kanna-1/project.git
   git push -u origin main
   ```

7. Confirmed **sync** between GitHub and the local folder (local `main` tracks `origin/main`).
8. Updated this `README.md` with help from cursor agent and committed and pushed to main with:

   ```bash
   git add README.md
   git commit -m "feat: updated README.md"
   git push origin main
   ```

## Current Status

- Research topic selected and scoped
- Expert list curated
- LinkedIn posts saved by author
- YouTube transcripts collected via API tooling
- Source annotations documented for later playbook creation
