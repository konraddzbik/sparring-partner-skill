---
tags: [sparring-partner, noise, operations]
max_turns: 12
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

Migration plan for our support tool's ticket routing:
- 3-week parallel run, covering weekends and the month-end peak. The new system runs in shadow mode: it computes routes but sends nothing (no notifications, no auto-replies, no SLA timers).
- Daily mismatch report split by queue and priority. A team lead triages every mismatch as old-wrong, new-wrong, or both acceptable.
- Cut-over gate: new-wrong rate under 0.5% overall AND zero new-wrong on P1/VIP tickets, for 7 consecutive days. If we don't hit it by the end of week 3, we extend by one week once, then stop and reassess.
- Rollback: one config flag, rehearsed in staging. Tickets created after cut-over are synced back to the old system by a nightly export, also rehearsed.
- Owner: me. Backup owner with rollback authority: Ana.

Anything wrong with it?
