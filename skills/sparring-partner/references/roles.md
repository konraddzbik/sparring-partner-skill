# Role lenses

Each role has typical blind spots and vocabulary. Challenge people in the language of their own
discipline: a framework they already respect lands better than a generic objection. Read only the
section you need. If the user's role is mixed (founder, team lead), combine two sections.

The blind spots below are *tendencies*, not accusations. Use them to know where to look, then
look at the actual artifact. Never open with "PMs always…".

## Contents
- Engineering
- Product
- Design / UX
- Marketing
- Sales
- People / HR / Recruiting
- Finance
- Leadership / Strategy
- Legal / Compliance / Risk
- Operations / Project delivery
- Data / Analytics

---

## Engineering

**Typical blind spots:** solving the interesting problem rather than the stated one; architecture
beyond team capacity; rewrites justified by taste; missing failure modes; no definition of done;
hidden consumers of the thing being changed.

**Questions that bite:**
- What's the smallest change that solves the stated problem? Why isn't that enough?
- What happens when the dependency is slow, down, or returns garbage?
- Who else reads this data or calls this API? How do you know the list is complete?
- How will you know it works after the next deploy, not just today?
- Is this a one-way door? If so, where's the ADR (context, decision, consequences)?

**For code review:** use the same output shape with `[severity] file:line — finding` issue lines,
severity order, noise budget. If the `critical-reviewer` skill is installed, it has a full code
quality checklist; this skill focuses on the decision and the reasoning behind the code.

## Product

**Typical blind spots:** falling for the solution before validating the problem; mistaking
stakeholder requests for user needs; vanity metrics; roadmaps as promises.

**Frameworks people respect:** the four product risks (value: will they buy or use it?;
usability: can they figure it out?; feasibility: can we build it?; viability: does it work for the
business: legal, sales, finance, brand?). Opportunity before solution.

**Questions that bite:**
- What evidence do you have that users have this problem, other than that someone asked for it?
- Which of the four risks is highest here, and what's the cheapest test for it?
- What will you *stop* doing to make room for this?
- What metric moves, by how much, and what would make you kill the feature?

## Design / UX

**Typical blind spots:** designing for the ideal user and the happy path; aesthetic consensus
standing in for evidence; edge states (empty, error, loading, long text, accessibility) left for
later.

**Questions that bite:**
- Who is the least experienced person who'll use this, and what do they do first?
- What did users *do* in testing (not what they said)?
- What does this look like empty, broken, in another language, with a screen reader?
- Which problem does this solve better than the current design, and how will you measure it?

## Marketing

**Typical blind spots:** confusing activity with impact; attributing every uptick to the last
campaign; messaging written for the team rather than the customer; no control group.

**Evidence people respect:** controlled experiments. At Bing, fewer than a third of ideas tested
in controlled experiments moved the metric they were designed to improve; a prior that "this
will work" should be modest.

**Questions that bite:**
- What's the hypothesis, and what result would prove it wrong?
- What would have happened without the campaign? Is there a holdout or a comparable region?
- Who exactly is the audience, and what do they currently believe that this message must change?
- Which metric is the goal and which are just leading indicators?

## Sales

**Typical blind spots:** happy ears (hearing commitment where there's interest); forecasting by
optimism; single-threaded deals; discounting to close instead of qualifying.

**Frameworks people respect:** structured qualification such as MEDDIC (Metrics, Economic buyer,
Decision criteria, Decision process, Identify pain, Champion) and its variants. Use it as a shared
checklist; its claimed win-rate effects come from vendors, not studies, so don't quote numbers.

**Questions that bite:**
- Have you met the economic buyer, or only the champion?
- What's their decision process and timeline, in their words, not yours?
- What happens to them if they do nothing? If the answer is "not much", why will this close?
- If this deal slips a quarter, what in your notes would have predicted it?

## People / HR / Recruiting

**Typical blind spots:** "culture fit" as a proxy for similarity; gut feel after unstructured
interviews; recency and halo effects in performance reviews; policies written for the one bad case.

**Evidence people respect:** structured interviews are the best-supported selection method in
the current meta-analytic estimates (validity ≈ .42 vs ≈ .19 for unstructured interviews; Sackett
et al., 2022, which revised the older, higher Schmidt & Hunter 1998 figures downward); consistent
criteria defined *before* seeing candidates.

**Questions that bite:**
- What were the criteria, and were they written down before you met the candidates?
- What evidence from the interview supports each rating, rather than an impression?
- Would you rate the same behaviour the same way from someone you like less?
- For a policy: who does this hurt that you didn't intend it for?

**Tone note:** people decisions are personal for someone. Be direct about the reasoning and
careful with the person; never speculate about protected characteristics, and flag legal review
where employment law is involved.

## Finance

**Typical blind spots:** the single-point forecast; hockey-stick growth; ignoring the base rate;
sensitivity untested; costs that scale differently than revenue.

**Evidence people respect:** reference-class forecasting: optimistic forecasts come from the
"inside view" (treating the project as unique), and overruns from optimism and sometimes strategic
misrepresentation (Kahneman & Lovallo, 1993; Flyvbjerg, 2006).

**Questions that bite:**
- What are the two or three inputs this model is most sensitive to? What happens at ±20%?
- What's the base rate for this kind of growth, payback or overrun in comparable cases?
- What's the downside case, and can the company survive it?
- Which assumptions came from the team that benefits from the number?

## Leadership / Strategy

**Typical blind spots:** goals mistaken for strategy; decisions made in a room without the people
who'll carry them; irreversible moves made as fast as reversible ones; teams agreeing because
disagreeing isn't safe.

**Frameworks people respect:** a strategy has a diagnosis (what's going on), a guiding policy (the
approach), and coherent actions; a list of ambitions is not a strategy. Reversible decisions
should be fast; irreversible ones slow and deliberate.

**Questions that bite:**
- What's the diagnosis? What's the one challenge this strategy is designed to overcome?
- What are you choosing *not* to do?
- Is this a one-way door? If not, why is it taking this long; if yes, why so fast?
- Who disagreed, and what was their best argument? If nobody did, is it safe to?
- Did the team fall for the proposal too early? Is the worst case bad enough? Were credible alternatives considered? (from Kahneman, Lovallo & Sibony's decision-review checklist)

## Legal / Compliance / Risk

**Typical blind spots:** treating every risk as equal; blocking instead of shaping; checklists
that miss the actual exposure; or, from the other side, business teams treating compliance as a
formality.

**Questions that bite:**
- Which of these risks is most likely and most damaging? Can you rank them?
- What's the cheapest control that removes most of the exposure?
- What's the cost of *not* doing this, including the risk of inaction?
- Who signs off, and does this need a qualified professional's review? (Say so explicitly.)

## Operations / Project delivery

**Typical blind spots:** plans with no slack; dependencies on people who weren't asked; status
reported green until it's red; process added for the one-time failure.

**Questions that bite:**
- What's the critical path, and what on it depends on someone outside your team?
- What's the earliest signal that this is slipping, and who watches it?
- What does this process cost every time, compared with the failure it prevents?
- What would you cut first if the deadline moved up two weeks?

## Data / Analytics

**Typical blind spots:** correlation sold as causation; metrics chosen after seeing the data;
small samples; survivorship; dashboards nobody decides anything with.

**Questions that bite:**
- What decision will this analysis change? If none, why do it?
- Was the metric and the threshold chosen before looking at the results?
- What else could explain this pattern? Have you ruled it out?
- Which piece of evidence actually discriminates between the explanations? Evidence consistent with every hypothesis proves nothing (Heuer's diagnosticity test; use the question, not the full ACH ritual).
- How big is the sample and the effect, and what's the uncertainty?
