---
type: project
title: Long-Distance Connected Lamp
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [esp32, supabase, iot, product, sri-lanka]
links: [[[confirmed-toolbox]]]
---

# Long-Distance Connected Lamp

Paired ESP32 lamps that sync colour state through Supabase polling.
Framed for the Sri Lankan market, primary use case: separated families.
Possible prototype and commercial exploration.

## Architecture decisions
- Two-rows pattern (one row per device, each reads the other's row) is
  the correct bidirectional sync pattern.
- **Polling is more reliable than Realtime WebSockets on ESP32.**
- The Supabase anon key should allow insert but not select on sensitive
  tables.
- Library: ESPSupabase.
