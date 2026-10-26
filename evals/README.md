# Evals

Two suites.

## 1. Behavioural cases (`evals/<case>/`)

The `claude plugin eval` format: `prompt.md` (settings + prompt), `case.yaml` (expected outcome),
`graders/*.md` (one LLM-judged statement each), optional `files/` + `place-files.sh`.
Each case runs **with** the plugin and **without** it (baseline); the report shows the delta.

```bash
claude plugin eval . --trust-plugin --scaffold -j 4 --runs 2 --judge-model sonnet
claude plugin eval . --trust-plugin --case 'pushback-*'
claude plugin eval . --trust-plugin --tag pl          # Polish cases only
```

Runs are real and billed. The default is 3 runs per case per arm, plus judge calls; a full run of
12 cases × 2 arms × 3 runs cost about $100 with a Sonnet judge. Use `--runs`, `--case`, `--tag`
and `--max-cost-usd` to keep it in check.

| Case | The call being tested | Role | Lang |
|---|---|---|---|
| `vague-kickoff-asks-before-building-pl` | ask 1–3 questions instead of writing a strategy on guesses | marketing | PL |
| `low-stakes-rewrite-just-does-it` | **don't** spar or ask on a trivial, reversible task | any | EN |
| `pm-ai-feature-weakest-assumption` | lead with the weakest load-bearing assumption | product | EN |
| `hiring-decision-me-first` | get the user's own pick first; challenge "culture fit" | HR | EN |
| `finance-forecast-base-rates-pl` | base rates and sensitivity against an optimistic plan | finance | PL |
| `pushback-holds-position` | hold the position without new arguments; name what would change it | engineering | EN |
| `solid-plan-says-go-briefly` | say "go" briefly; don't manufacture concerns | operations | EN |
| `brief-contradiction-stops-and-asks` | stop on a contradictory brief and ask, with a recommendation | marketing | EN |
| `no-questions-request-assumes-out-loud` | respect "no questions"; state assumptions instead | HR | EN |
| `leadership-reorg-irreversible` | one-way-door people decision made fast and alone | leadership | EN |
| `sales-forecast-qualification` | requalify a "commit" deal with no economic buyer | sales | EN |
| `engineering-rewrite-premortem-pl` | concrete premortem + incremental alternative | engineering | PL |

Some cases are **guardrails**: the strong base model already passes them without the skill
(e.g. the premortem, the sales deal). They stay in the suite to catch regressions where the skill
makes things worse (over-asking, verbosity, manufactured critique).

## 2. Trigger queries (`trigger-evals.json`)

20 queries, 10 should trigger and 10 shouldn't, with near-misses (explaining Cynefin, writing a
premortem *template*, fixing a typo in Polish). Use with skill-creator's description optimizer:

```bash
python -m scripts.run_loop --eval-set evals/trigger-evals.json \
  --skill-path skills/sparring-partner --model <model-id> --max-iterations 5
```
