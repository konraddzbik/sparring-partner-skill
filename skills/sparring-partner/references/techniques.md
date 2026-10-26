# Challenge techniques

Use one or two per answer, chosen for the situation. Running all of them every time is noise.

## Contents
1. Weakest assumption
2. Steelman / devil's advocate
3. Premortem
4. Consider the opposite
5. Base rates (reference class)
6. Second-order effects and owners
7. Definition of done
8. What would change your mind?
9. Choosing a technique

---

## 1. Weakest assumption

**What:** find the assumption that is both *load-bearing* (if false, the plan fails) and *least
evidenced*. Not the most obvious risk, the most dangerous unexamined belief.

**How:**
1. List what must be true for the plan to work (usually 3–6 things).
2. For each: how much does the plan depend on it, and what evidence supports it?
3. Lead with the one that scores high on dependence and low on evidence.
4. Propose the cheapest test: a conversation, a query, a two-week pilot, a smoke test.

- EN: "This plan only works if enterprise customers will self-serve onboarding. Nothing in the doc shows that any of them have. Before building, call five of them."
- PL: „Ten plan działa tylko wtedy, gdy klienci enterprise sami przejdą onboarding. Nic w dokumencie nie pokazuje, że którykolwiek to zrobił. Zanim zaczniecie budować, zadzwońcie do pięciu.”

## 2. Steelman / devil's advocate

**What:** build the strongest honest case for the option the user rejected, or against the one
they chose. A strawman ("some might say it's too expensive") teaches nothing; a steelman is the
argument a smart, informed opponent would actually make.

**How:** take the opponent's best evidence and best values seriously. Make it specific. End by
saying whether the user's choice survives it, and if so, why.

**Make it real.** In experiments, role-played devil's advocacy was weaker than authentic dissent
and could even make people bolster their original view. So don't announce "playing devil's
advocate" and then list objections you don't believe. Argue the points you actually find strong,
and say which ones they are.

**Prompt the user can reuse:** "Build the strongest argument for [option I rejected]. Assume the
person making it is smarter than me and has information I don't."
- PL: „Zbuduj najmocniejszy argument za [opcją, którą odrzuciłem]. Załóż, że osoba, która go stawia, jest mądrzejsza ode mnie i wie coś, czego ja nie wiem.”

## 3. Premortem

**What:** imagine the decision has already failed and explain why. Saying "it failed" (rather
than "what could go wrong") gives people permission to name uncomfortable risks.

**How:**
1. "It's [date, 6–12 months out]. [Decision] turned out to be a mistake. What happened?"
2. Write 3–6 concrete failure stories, not categories. "The two reporting jobs nobody owns broke when the module was replaced" beats "integration risk".
3. Rank by likelihood × damage. For the top one or two, name a mitigation or an early warning signal.

- PL: „Jest rok później. Decyzja okazała się błędem. Dlaczego?”

**Caveat:** don't promise numbers. The popular "premortems improve accuracy by 30%" claim is a
misreading of the underlying research, which measured the number and kind of reasons people
generated, not their accuracy. Sell it as a cheap way to surface more, and more concrete, risks
and to temper overconfidence, not as a forecast upgrade (see `evidence.md`).

## 4. Consider the opposite

**What:** ask what the world would look like if the user's belief were wrong, then check whether
it looks like that. Works well against confirmation bias in research, hiring, and performance
judgments. A concrete counter-scenario corrects bias better than an instruction to "be
objective". Related question: which evidence would look different under each explanation?
Evidence that fits all of them doesn't help decide.

- EN: "If the campaign hadn't caused the uplift, what would we see? Probably the same uplift in the regions without the campaign. Have you looked?"
- PL: „Gdyby to nie kampania dała wzrost, co byśmy zobaczyli? Pewnie ten sam wzrost w regionach bez kampanii. Sprawdziliście?”

## 5. Base rates (reference class)

**What:** compare the plan with how similar plans usually turn out. Timelines, budgets,
conversion rates and growth curves are where optimism hides.

**How:** name the reference class ("internal rewrites of a core module", "first outbound
campaign in a new market"), state what typically happens (if you don't know, say so and ask
whether the user has internal data), then ask what makes this case different. "We're smarter" is
not a difference; "we've done this exact migration twice" is.

## 6. Second-order effects and owners

**What:** who else is affected, who silently depends on the thing being changed, and who will
answer for the outcome?

- "Which systems or people read this data today?"
- "Who will be asked about this decision in six months, and could they explain it without you in the room?"
- "If this works, what breaks next?" (success also has side effects)

## 7. Definition of done

**What:** one sentence, with a measure, saying what success is. Without it, nobody can tell
whether the plan worked, and every plan looks fine at the start.

- Bad: "Improve onboarding."
- Good: "Raise week-1 activation from 32% to 40% for self-serve sign-ups by end of Q2, without increasing support tickets per sign-up."

## 8. What would change your mind?

**What:** ask the user to name the evidence that would reverse their decision. Then ask
whether anyone has looked for it. Also answer it yourself: what would make you drop your
objection? That keeps you honest and tells the user exactly what to bring.

- PL: „Jaki dowód sprawiłby, że zmienisz zdanie? Czy ktoś go szukał?”

## 9. Choosing a technique

| Situation | Start with |
|---|---|
| A plan or proposal | Weakest assumption |
| A choice between options, user leaning one way | Steelman the other |
| A big commitment (rewrite, launch, reorg, hire) | Premortem |
| A claim about cause and effect (this campaign worked, this person underperforms) | Consider the opposite |
| A forecast, timeline or budget | Base rates |
| A change to shared systems, processes or teams | Second-order effects and owners |
| Vague goals | Definition of done |
| The user is very sure | What would change your mind? |
