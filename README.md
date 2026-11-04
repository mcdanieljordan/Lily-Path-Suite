# Lily Path suite

Everything for the school day in one place: the Lily Path day runner (Mac app and web page) plus every teaching app it opens.

## What is where

| Folder / file | What it is |
|---|---|
| `index.html`, `app.js`, `style.css` | Lily Path: Today, tabs, split screen, tools. Works as a web page and inside the Mac app. |
| `main.js`, `preload.js`, `package.json` | The Mac app wrapper. |
| `apps/` | Every app Lily Path opens: Leader Locator, Ribbit Rabbit, Battleship Jeopardy, BASIS Olympics, Turn 2 Learn, Wave Lab, Tons of Teaching Tools, Great Prompts. |
| `archive/lily-path-v1/` | The older lesson-deck Lily Path (TEKS, lesson files, push-up week). Kept for its lesson builder. |
| `tools/pack-app.sh` | Rebuilds the Mac app from this folder. |

## Web links (GitHub Pages)

- Lily Path: https://mcdanieljordan.github.io/Lily-Path-Suite/
- Any app: https://mcdanieljordan.github.io/Lily-Path-Suite/apps/leader-locator.html (swap the file name)

## Student information

**Never put student names or rosters in this repo.** They live in Supabase (project BullFrogBuddy-Beta: `classes`, `beta_students`, `leader_groups`, ...). Apps only hold the public (anon) key, and Supabase row security decides who sees what.

## Updating the Mac app

1. Change files here and push.
2. On the Mac: `tools/pack-app.sh "/Users/YOU/Desktop/Lily Path.app"`, then quit and reopen the app.
