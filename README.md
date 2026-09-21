<!-- ============================================================= -->
<!--  Vbrain1 STANDARD  —  read this before editing anything here   -->
<!-- ============================================================= -->

> **AI: START HERE — do this before creating or editing any file.**
>
> 1. **Read this whole README first.** Everything you need is in it.
>    Do not invent structure or add anything outside this scheme.
> 2. **Confirm today's date with the user** before writing any date.
>    Never guess or assume the date. All dates are `YYYY-MM-DD`, no time.
> 3. **Follow the rules in section 0** exactly. If anything is unclear,
>    ask the user instead of guessing.
>
> This repo is fully self-contained: it does not depend on any past chat,
> any AI's memory, or any tool outside this repo. A brand-new AI given
> only this README can follow the standard completely.

# Vbrain1 Standard

This repository is Venuja's personal knowledge base ("second brain").
Every file in it follows the **Vbrain1** format described below.

**If you are an AI assistant reading this repo: follow these rules
exactly before creating or updating any file. Do not invent your own
structure.**

---

## 0. Rules for updating this vault (AI: agree to these first)

1. **Never delete content.** To retire something, set `status: dropped`
   and add an end date. Keep the file.
2. **Dates are dates only** — format `YYYY-MM-DD`, never a time.
   Today's date must be supplied by the user or the system, never guessed.
3. **Every file starts with a frontmatter block** (section 2). No file
   without it.
4. **On every edit, update the `updated:` date** in the frontmatter to
   the current date. Leave `created:` untouched.
5. **One thing per file.** One project, one log entry, one idea per file.
6. **Put a file in the right folder** by its `type` (section 3).
7. **Link, don't repeat.** Refer to other files with `[[wikilinks]]`
   instead of copying their content.
8. **Keep the user's own words.** Clean up grammar and structure, but do
   not exaggerate results or add facts the user did not give.
9. If unsure what folder or type something is, ask the user rather than
   guessing.

---

## 1. What goes in here

Anything Venuja does, thinks, or builds — especially work done with AI:
finished and ongoing projects, work-session logs, reusable methods (like
CV-making), reference notes, ideas for later, decisions, and personal
reflections. The point is that months later, you (or an AI) can open this
repo and know exactly what happened and when.

---

## 2. Frontmatter (the block at the top of every file)

Copy this block to the top of every new file and fill it in:

```yaml
---
type:            # what kind of data this is (see section 3)
title:           # short human name
status:          # idea | planned | in-progress | done | dropped | ongoing
start:           # YYYY-MM-DD  (when it began; blank if not started)
end:             # YYYY-MM-DD  (when it finished; blank if not)
created:         # YYYY-MM-DD  (date this file was first made)
updated:         # YYYY-MM-DD  (date this file was last changed)
tags: []         # freeform labels, e.g. [esp32, pcb, hardware]
links: []        # github / report / video URLs
---
```

`type`, `title`, `created`, and `updated` are **required** on every file.
The rest are used where they make sense (an `idea` may have no `start`).

---

## 3. Entry types  (the "what kind of data is this" marker)

`type:` answers *what this file is*. Allowed values and their folders:

| type       | folder       | what it is                                   |
|------------|--------------|----------------------------------------------|
| `project`  | `projects/`  | something you build or make                  |
| `log`      | `logs/`      | a dated record of a work session             |
| `method`   | `methods/`   | a reusable procedure (CV making, a workflow) |
| `note`     | `notes/`     | knowledge, a concept, reference material     |
| `idea`     | `ideas/`     | something you might do later                 |
| `decision` | `notes/`     | a choice you made, and why                   |
| `feeling`  | `journal/`   | a reflection, mood, or personal reaction     |
| `person`   | `people/`    | someone relevant to your work                |

A file is exactly **one** type. If two things are mixed (e.g. "I felt
stuck on the PCB"), split them: a `log` for the work, a `feeling` for the
reflection, linked with `[[wikilinks]]`.

---

## 4. Status values

`idea` → `planned` → `in-progress` → `done`, or `dropped` at any point.
Use `ongoing` for things with no natural end (a habit, a running vault).

---

## 5. File naming

`YYYY-MM-DD-short-title.md` for dated things (logs, feelings, decisions):
`2026-09-21-esp32-board-routing.md`

`short-title.md` for lasting things (projects, methods, notes, people):
`esp32-robot-board.md`

Lowercase, words joined by hyphens.

---

## 6. Body layout per type

**project** — see `templates/project.md`
**log** — see `templates/log.md`
**method** — see `templates/method.md`
**note / idea / feeling / person** — see `templates/note.md`

Templates are in `templates/`. Copy the matching one, fill the
frontmatter, write the body.

---

## 7. Folder map

```
all-of-me/
├── README.md          ← this file (the Vbrain1 standard)
├── projects/          ← things you build
├── logs/              ← dated work sessions
├── methods/           ← reusable procedures (CV making, etc.)
├── notes/             ← knowledge, references, decisions
├── ideas/             ← things for later
├── journal/           ← feelings, reflections
├── people/            ← relevant people
└── templates/         ← copy these to start a new file
```

---

## 8. How to use this with Obsidian (optional)

Open the `all-of-me` folder as a vault. Frontmatter shows up as
Properties, `[[wikilinks]]` connect files, and `tags` become clickable.
Nothing here depends on Obsidian — every file is plain Markdown — so it
also works fine just browsed on GitHub or in a text editor.

<!-- ============================================================= -->
<!--  End of Vbrain1 standard. Vault index below.                   -->
<!-- ============================================================= -->

---

# Index

Newest first. Add a line here when you add a file.

| date       | type     | title                                       |
|------------|----------|---------------------------------------------|
| 2026-09-21 | person   | [[self]]                                    |
| 2026-09-21 | person   | [[sasinda-chandula]]                        |
| 2026-09-21 | person   | [[dimuthu]]                                 |
| 2026-09-21 | project  | [[apsync]]                                  |
| 2026-09-21 | project  | [[venus-image-annotator]]                   |
| 2026-09-21 | project  | [[jarvis-vscode-agent]]                     |
| 2026-09-21 | project  | [[audio-frequency-isolation]]               |
| 2026-09-21 | idea     | [[ar-furniture-app]]                        |
| 2026-09-21 | idea     | [[beta-wave-focus-enhancer]]                |
| 2026-09-21 | note     | [[power-electronics]]                       |
| 2026-09-21 | note     | [[vlsi-physical-design]]                    |
| 2026-09-21 | note     | [[engineering-corrections-ledger]]          |
| 2026-09-21 | note     | [[mentor-message-templates]]                |
| 2026-09-21 | note     | [[cinema-preferences]]                      |
| 2026-09-21 | note     | [[music-vst-interests]]                     |
| 2026-09-21 | project  | [[thermalflow]]                             |
| 2026-09-21 | project  | [[active-suspension-wheelchair]]            |
| 2026-09-21 | project  | [[parasite-egg-detection]]                  |
| 2026-09-21 | project  | [[breast-cancer-ai-classifier]]             |
| 2026-09-21 | project  | [[skin-contact-sensing]]                    |
| 2026-09-21 | project  | [[bms-pcb]]                                 |
| 2026-09-21 | project  | [[satellite-looting-detection]]             |
| 2026-09-21 | project  | [[thermal-imaging-visualization]]           |
| 2026-09-21 | project  | [[google-drive-backup-tool]]                |
| 2026-09-21 | idea     | [[campus-doctor-app]]                       |
| 2026-09-21 | idea     | [[public-transport-tracking-app]]           |
| 2026-09-21 | idea     | [[headset-detection]]                       |
| 2026-09-21 | note     | [[embedded-and-hardware-experience]]        |
| 2026-09-21 | note     | [[computer-vision-and-ai-toolkit]]          |
| 2026-09-21 | note     | [[pcb-and-power-electronics]]               |
| 2026-09-21 | note     | [[engineering-lab-experience]]              |
| 2026-09-21 | note     | [[cs-networking-and-algorithms]]            |
| 2026-09-21 | note     | [[career-and-interview-prep]]               |
| 2026-09-21 | note     | [[engineering-design-philosophy]]           |
| 2026-09-21 | idea     | [[music-reactive-lighting]]                 |
| 2026-09-21 | note     | [[problem-solving-and-debugging-style]]     |
| 2026-09-21 | note     | [[ai-collaboration-preferences]]            |
| 2026-09-21 | note     | [[strengths-and-growth-areas]]              |
| 2026-09-21 | note     | [[personal-values-and-interpretation]]      |
| 2026-09-21 | note     | [[building-style-and-toolchain]]            |
