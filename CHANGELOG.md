# Changelog

All notable changes to this project are documented here. Versions follow the `version` field in
`.claude-plugin/plugin.json`. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] — unreleased

### Added
- `sparring-partner` skill: three modes (automate / oracle / sparring) chosen by three questions;
  clarification gate (ask vs. assume out loud); "me first" on decisions; challenge toolkit; anti-sycophancy
  rules; role-neutral verdict scale (stop / rethink / conditional / go / strong, with Polish equivalents);
  noise budget; mid-project stop rule; `.sparring-partner.md` project config.
- References: `clarification.md`, `techniques.md`, `roles.md` (11 role lenses), `evidence.md`.
- `examples.md`: eight worked examples across roles, EN/PL.
- `devils-advocate` read-only agent for unanchored second opinions.
- Eval suite: 12 behavioural cases (`claude plugin eval` format) and 20 trigger queries.
- CI: manifest lint, verdict-term consistency, eval-case shape, SKILL.md length, `claude plugin validate --strict`.
- `research/`: deck sources (PL) and external research (clarification, sycophancy, challenge techniques, skill authoring, role frameworks).
- `evals/RESULTS.md`: four eval iterations; mean score 0.90 with the skill vs 0.72 without.

### Changed during evaluation
- Clarification: answer-and-ask in the same turn by default; stated assumptions aren't extra questions.
- Anti-sycophancy: turn confident claims into questions before judging; always name what would change your mind; short pushback replies.
- Me first made explicit for "which should I pick?" requests.
- Authentic, not role-played, challenge; one-line steelman of the user's position.
- Short form for sound plans; description shortened to under 1,024 characters and broadened to strategy/plan/brief kickoffs.

### Derived from
- `critical-reviewer` 3.1.0 (stance, noise budget, artifact-focused tone), with one deliberate change:
  ask instead of guessing when a wrong guess is costly.
- The talk "Od automatyzacji do symbiozy" (AI Collective Wrocław, 28.10.2026) and its fact-checked sources.
