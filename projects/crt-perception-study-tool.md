---
type: project
title: CRT Perception Study Tool (Web App)
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [research-tooling, web-app, supabase, streamlit, biomedical]
links: [[[dengue-crt-wearable]]]
---

# CRT Perception Study Tool

Web app used to gather ground-truth data for [[dengue-crt-wearable]]:
medical professionals watch CRT videos and mark the exact frame where
skin colour returns. Marks from many participants are combined into a
consensus ground-truth frame per video, compared against the automatic
algorithm.

## v1 — local web app
`index.html`, `styles.css`, `excel_helper.py`, `convert_videos.py`,
videos folder, README, distributed via GitHub. Each student runs it
locally; results go to their own `data.xlsx`, merged later. No login —
just a participant name (not real identity), role, age group, video
info, and marked time/frame.

## Recording pipeline
Arduino automatic stamping, re-encoded with a green colour frame added,
saved with `.stamp.json` metadata (video filename, trigger_source,
frame_count, recording_duration_s, fps, stamped, stamped_frame,
stamp_time_s, post_stamp_tail_s).

## v2 — hosted version
Migrated to a **Supabase** backend with a **Streamlit** analysis
dashboard.
