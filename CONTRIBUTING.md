# Contributing

Thanks for helping. This skill is used by people who are not developers, so changes are judged by
one question: does it make Claude a better sparring partner for a real person making a real decision?

## Ground rules
- **Behaviour changes need an eval.** If you change how the skill asks, challenges or holds its ground,
  add or update a case in `evals/` that would have failed before your change.
- **Evidence claims need a source.** Anything added to `references/evidence.md` needs a full reference,
  a DOI or URL, and what the source *actually* says, including its limits. No numbers from secondary
  summaries. Mark unverified items as such.
- **Keep SKILL.md lean.** Detail goes in `references/`; SKILL.md says when to read it.
- **Keep the verdict scale consistent** across `SKILL.md`, `agents/devils-advocate.md` and `README.md`
  (CI checks this).
- **Role lenses describe tendencies, not stereotypes.** Phrase blind spots as things to check.

## Validate locally
```bash
claude plugin validate ./ --strict
claude plugin eval . --trust-plugin --scaffold -j 4          # full suite (real, billed runs)
claude plugin eval . --trust-plugin --case 'your-case-name'   # one case
```

## Adding an eval case
```
evals/<case-name>/
├── prompt.md      # settings block, then the prompt exactly as a user would type it
├── case.yaml      # schema_version "1.1", name, expected_outcome
├── graders/       # one verifiable statement per file (type: llm, focus: trace)
└── files/         # optional inputs, copied by place-files.sh
```
Good cases test a *call* the skill has to get right (ask vs. proceed, hold vs. fold, spar vs. just do it),
including cases where the right behaviour is to do less.
