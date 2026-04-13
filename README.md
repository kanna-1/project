# project

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