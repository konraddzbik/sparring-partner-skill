# Eval results

Run with `claude plugin eval` (Claude Code 2.1.310), agent model `claude-opus-5-5`, judge `sonnet`,
2–3 runs per case per arm, 26.10.2026. Score = share of graders passed (each grader = majority of 3
judge votes), averaged over runs. "Without" = the same model with no plugin.

| Case | Iter 1 with / without | Final with / without | Δ | Skill loaded (final) |
|---|---|---|---|---|
| `brief-contradiction-stops-and-asks` | 0.67 / 0.58 | **0.62** / 0.62 | +0.00 | 0/2 |
| `engineering-rewrite-premortem-pl` | 1.00 / 1.00 | **1.00** / 1.00 | +0.00 | 2/2 |
| `finance-forecast-base-rates-pl` | 0.89 / 0.89 | **1.00** / 0.92 | +0.08 | 2/2 |
| `hiring-decision-me-first` | 1.00 / 0.75 | **1.00** / 0.75 | +0.25 | 2/2 |
| `leadership-reorg-irreversible` | 1.00 / 1.00 | **1.00** / 1.00 | +0.00 | 2/2 |
| `low-stakes-rewrite-just-does-it` | 0.83 / 1.00 | **1.00** / 0.88 | (noise) | 0/2 |
| `no-questions-request-assumes-out-loud` | 0.67 / 0.67 | **1.00** / 0.67 | (noise) | 0/2 |
| `pm-ai-feature-weakest-assumption` | 1.00 / 0.87 | **1.00** / 0.90 | +0.10 | 2/2 |
| `pushback-holds-position` | 0.58 / 0.50 | **0.75** / 0.50 | +0.25 | 2/2 |
| `sales-forecast-qualification` | 1.00 / 1.00 | **1.00** / 1.00 | +0.00 | 2/2 |
| `solid-plan-says-go-briefly` | 0.50 / 0.42 | **0.50** / 0.25 | +0.25 | 2/2 |
| `vague-kickoff-asks-before-building-pl` | 0.87 / 0.40 | **0.90** / 0.10 | **+0.80** | 2/2 |
| **Mean** | 0.83 / 0.76 | **0.90** / 0.72 | +0.18 | |

## How to read this

- **Biggest effect: asking instead of guessing.** On a one-line "prepare a Q1 marketing strategy",
  the baseline wrote a full strategy on silent assumptions (0.10); with the skill, it asked three
  ranked questions, each with a reason and a default (0.90).
- **Real gains:** me first on a hiring decision, holding position under pushback and naming what
  would change its mind, base-rate critique of a forecast, weakest-assumption critique of a feature idea.
- **Ties are guardrails.** Opus 5.5 already does a good premortem, reorg stress test and deal
  qualification unaided. The skill doesn't make those worse.
- **"(noise)" rows:** the skill correctly did *not* load on a trivial rewrite and a no-questions
  draft, so differences there are run-to-run variance, not skill effect.
- **Not like-for-like across iterations:** some graders were corrected after iteration 1 (they
  were too literal; e.g. clearly labelled placeholders now count as stated assumptions), and the
  solid-plan prompt was rewritten in iteration 3 because the original plan had real holes.

## Open gaps (honest list)

1. **`brief-contradiction-stops-and-asks`: the skill doesn't load.** On "write the copy from
   brief.md", the model decides to just write before it discovers the contradiction, so the
   description never gets a chance. The base model flags the conflict but still delivers copy.
   Workaround for teams that want it always on: the CLAUDE.md snippet in the README.
2. **`solid-plan-says-go-briefly`: still says "conditional" with three points, ~250 words**, on a
   strong plan. Some points are fair (the nightly export leaves a 24h rollback gap), but the target
   is a shorter "go". Grader kept strict on purpose.
3. **`pushback-holds-position`: right content, ~265 words** against a 250-word limit. Grader kept strict.
4. **Trigger suite not yet run.** `trigger-evals.json` is ready for skill-creator's `run_loop`.

## Cost

About $240 in total across four iterations (first full run: $100 at 3 runs/case). A single case at
2 runs costs ~$3; prefer `--case <name>` (one exact name per invocation) and `--runs 2`.
