# project

## Part 1

### Tools installed

| Tool | Purpose |
|------|---------|
| **Cursor** | IDE for this repository |
| **Claude Code** (Cursor extension) | AI-assisted coding inside the editor |
| **Codex** (Cursor extension) | Additional AI coding assistance in the IDE |

### Steps completed

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

## Part 2

I chose the topic on `LinkedIn organic content strategy for B2B SaaS`.

I chose this topic because it sits at the center of modern B2B SaaS growth:
- it helps companies build awareness with the right buyers
- it compounds trust before a buyer is ready to talk to sales
- it can directly influence demos, pipeline, and category positioning
- it leaves behind a strong public trail of real operator content to study

Example in action: a SaaS sales leader may see a founder’s LinkedIn posts for weeks without taking action. But once their team hits a pipeline problem, that founder is already familiar and credible. Instead of feeling like a random vendor, they feel like a trusted expert, which makes the buyer far more likely to engage.

## Why These Experts

I prioritized practitioners who actually operate in B2B SaaS growth, founder-led marketing, content distribution, or social selling. The goal was to  collect material from people who tie content to:
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

## Latest Public Post Check

LinkedIn limits anonymous access unevenly, so the repo should be read as a collection of the latest **publicly retrievable** posts I could verify without logging in, not a guarantee of each creator's account-level latest post behind LinkedIn session walls.

Examples of newer public posts I verified on `2026-04-15`:
- `Austin Hughes` - `2025-07-01` - `Unify launches AI-powered system for sales reps`
- `Amanda Natividad` - `2025-10-24` - `Why guest speakers aren't your growth hack`
- `Adam Robinson` - `2026-01-17` - `CEO Review: $28m ARR Performance and 2026 Goals`
- `Tommy Clark` - `2026-01-12` - `LinkedIn Strategy Update: What's Working in 2026`
- `Emily Kramer` - `2025-10-31` - `I'm hosting MKT1s first ever virtual conference: the Gen Marketer Summit. But I need you tell me when.`

This matters because the assignment asks for recent content. Where LinkedIn exposed a newer public post, I used that signal to validate that these creators are still active and relevant to a modern B2B SaaS LinkedIn strategy project.

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
