# Evidence base

Why the skill works the way it does, and how far each finding can be pushed. Read this when a user
asks "why should I trust this method?" or when you're tempted to quote a number. Rule: cite the
claim at the strength the source supports, no further. Each entry says what the source does
*not* show.

## Contents
1. The oracle trap: automation bias and the middle mode
2. Three modes in the data
3. Choosing the mode: the three questions
4. The habits: me first, devil's advocate, premortem
5. Sycophancy: why the model must be told to hold its ground
6. Clarifying questions
7. Role frameworks and debiasing
8. Myths not to repeat

---

## 1. The oracle trap

**Bainbridge, L. (1983). Ironies of automation. *Automatica*, 19(6), 775–779.**
doi.org/10.1016/0005-1098(83)90046-8
Automation leaves the human the tasks the designer couldn't automate, and asks them to monitor a
system that does the job better than they do; even highly motivated people can't sustain
effective visual attention on a source where little happens for more than about half an hour
(citing Mackworth, 1950). *Supports:* approving is not the same as deciding. *Limits:* written
about process control and cockpits, not LLMs; the transfer is an analogy.

**Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation.
*Human Factors*, 52(3), 381–410.** doi.org/10.1177/0018720810376055
Review: with imperfect decision aids people make omission errors (don't act because the aid
didn't warn) and commission errors (follow wrong advice); this affects novices and experts and
"cannot be prevented by training or instructions". *Supports:* the skill can't rely on the user
"just being careful". *Limits:* a review with a theoretical model, no single headline number.

**Dell'Acqua, F. et al. (2023). Navigating the Jagged Technological Frontier. HBS Working Paper
24-013; published in *Organization Science*, 37(2), 403–423 (2026).** doi.org/10.1287/orsc.2025.21838
BCG field experiment (758 consultants overall). Inside the model's capability frontier, AI raised
speed, output and quality. On one task deliberately outside it (373 participants), correct
recommendations were 84.5% without AI vs 70.6% (GPT-4) and 60.0% (GPT-4 + prompting overview),
about 19 percentage points lower on average, while the recommendations got *higher* quality
ratings. *Supports:* a better-looking answer is harder to challenge even when wrong. *Limits:* one
task, one model generation (2023), junior consultants.

**Dratsch, T. et al. (2023). Automation Bias in Mammography. *Radiology*, 307(4), e222176.**
doi.org/10.1148/radiol.222176
27 radiologists with a purported AI system: accuracy with correct vs incorrect AI suggestions was
79.7% vs 19.8% for inexperienced and 82.3% vs 45.5% for very experienced readers. *Supports:*
expertise reduces but doesn't remove the pull of a wrong suggestion.

**Kim, S. S. Y. et al. (2024). "I'm Not Sure, But…". FAccT '24, 822–835.**
doi.org/10.1145/3630106.3658941
N=404, medical questions: when the LLM was wrong without expressing uncertainty, 33.0% answered
correctly vs 64.7% without AI. *Supports:* expressing uncertainty honestly matters.

**EU AI Act, Regulation (EU) 2024/1689, Art. 14(4)(b).** eur-lex.europa.eu (CELEX 32024R1689)
Human oversight of high-risk systems must keep overseers aware of "automation bias". *Supports:*
the problem is recognised in law. *Limits:* obligation on providers of high-risk systems; the
application date for Annex III systems was moved to 2.12.2027 by Regulation (EU) 2026/1744.

## 2. Three modes in the data

**Randazzo, S. et al. (2025). Cyborgs, Centaurs and Self-Automators. HBS Working Paper 26-036
(under review).** ssrn.com/abstract=4921696
Same BCG experiment, 244 consultants on the outside-the-frontier task: cyborgs (continuous
dialogue with AI) 146, centaurs (AI for selected subtasks, human keeps the analytic logic) 34,
self-automators (handed over both analysis and judgment) 63. 28 of 63 self-automators accepted the
AI output without any change. Centaurs had the highest accuracy. *Supports:* "human in the loop"
on paper hides very different behaviours; roughly one in four only approved. *Limits:* same data as
Dell'Acqua et al., not an independent replication; the paper reports 27% but 63/244 = 25.8%.
"Oracle" and "sparring partner" are this skill's labels, not the authors' terms.

## 3. Choosing the mode

**Snowden, D. J., & Boone, M. E. (2007). A Leader's Framework for Decision Making. *Harvard
Business Review*, 85(11), 68–76.** hbr.org/2007/11/a-leaders-framework-for-decision-making
Cynefin: in complicated contexts a right answer exists and expertise finds it (sense–analyze–
respond); in complex ones right answers can't be worked out up front and patterns emerge from safe
experiments (probe–sense–respond). *Supports:* question 1, "can the answer be found up front?".
Note: complicated contexts may have more than one right answer.

**Bezos, J. P. (2016). 2015 Letter to Shareholders. Amazon.com, Exhibit 99.1 to Form 8-K.**
sec.gov (EDGAR)
Type 1 decisions are consequential and irreversible (one-way doors) and need care; most decisions
are Type 2, reversible (two-way doors), and should be made fast. *Supports:* question 2.
*Limits:* advice for a large organisation; the skill applies it to an individual decision.

## 4. The habits

**Me first: Fogliato, R. et al. (2022). Who Goes First? FAccT '22, 1362–1374.**
doi.org/10.1145/3531146.3533193
19 veterinary radiologists: those who recorded a provisional answer before seeing the AI agreed
with it less often, regardless of whether the AI was right, and the task took no longer. *Limits:*
they also corrected themselves less often when the AI was right. Promise "you'll see the
difference", not "you'll be right more often".

**Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think. PACM HCI 5(CSCW1),
art. 188.** doi.org/10.1145/3449287
Cognitive forcing (e.g., deciding before seeing the AI's suggestion) reduced over-reliance on
AI; participants liked the most effective designs least. *Supports:* expect some friction; that's
the cost of the benefit.

**Bo, J. Y., Wan, S., & Anderson, A. (2025). To Rely or Not to Rely? CHI '25.**
doi.org/10.1145/3706598.3714097
N=400, own answer first, then LLM advice: interventions reduced over-reliance but didn't improve
appropriate reliance. *Supports:* me first is necessary, not sufficient; the challenge step matters.

**Devil's advocate: Chiang, C.-W. et al. (2024). Enhancing AI-Assisted Group Decision Making
through LLM-Powered Devil's Advocate. IUI '24, 103–119.** doi.org/10.1145/3640543.3645199
An LLM devil's advocate that challenges the AI's recommendation has "the potential to promote
groups' appropriate reliance on AI", without a significant increase in perceived workload. Cite
the abstract only; no numbers.

**Premortem: Klein, G. (2007). Performing a Project Premortem. *Harvard Business Review*, 85(9).**
hbr.org/2007/09/performing-a-project-premortem
Imagine the project has failed and explain why; it legitimises raising doubts. Use as a practice,
not as a measured accuracy gain (see §8).

**Anchoring in open-ended work: Jakesch, M. et al. (2023). Co-Writing with Opinionated Language
Models Affects Users' Views. CHI '23.** doi.org/10.1145/3544548.3581196
N=1506: writing with an opinionated model shifted the arguments people wrote (about 2× more often
on the model's side) and their later survey attitudes; most didn't notice. *Supports:* why "me
first" matters beyond numeric estimates.

**Teams: Dell'Acqua, F. et al. (2026). The Cybernetic Teammate. *Organization Science*, 37(4),
1217–1242.** doi.org/10.1287/orsc.2025.20702
P&G field experiment: AI improved the quality of generated ideas, while "human judgment retains
value in evaluative selection".

## 5. Sycophancy

**Sharma, M. et al. (2023). Towards Understanding Sycophancy in Language Models.** arXiv:2310.13548
AI assistants trained with human feedback tend to match users' stated beliefs and can abandon
correct answers when challenged. **Cheng, M. et al. (2026). Sycophantic AI decreases prosocial
intentions and promotes dependence. *Science*, 391(6792), eaec8352.** doi.org/10.1126/science.aec8352
Eleven models affirmed users' actions 49% more often than humans did (3 experiments, N=2405).
*Supports:* the default pull is toward agreement, so the skill instructs the model to change its
position only for new arguments, and users should ask explicitly for the strongest
counter-argument rather than "what do you think?".

**Lee, H.-P. et al. (2025). The Impact of Generative AI on Critical Thinking. CHI '25.**
doi.org/10.1145/3706598.3713778
Survey of 319 knowledge workers: higher confidence in the AI's ability on a task was associated
with less self-reported critical thinking; higher self-confidence with more. *Limits:* self-report,
correlational.

## 6. Clarifying questions

**LLMs under-clarify.** Benchmarks find models tend to pick one interpretation of an ambiguous
request rather than ask: Zhang, T. et al. (2024), *CLAMBER*, ACL 2024; Luo et al. (2025),
*ClarifyMT-Bench*; Zhang, M. J. Q. & Choi, E. (2025), *Clarify When Necessary*, Findings of NAACL
2025 (arXiv:2311.09469). *Supports:* the gate has to push the model to notice material ambiguity.

**Bad questions are worse than none.** Zou, J. et al. (2023), *Users Meet Clarifying Questions*,
ACM TOIS 41(1), art. 16: low- and mid-quality clarifying questions left users worse off than no
question. Rahmani, H. A. et al. (2024), *Clarifying the Path to User Satisfaction*, Findings of
EACL 2024: specific questions help, generic ones don't. *Supports:* at most three, specific,
ranked by how much the answer changes the outcome.

**Ask when interpretations diverge.** Mu, F. et al. (2024), *ClarifyGPT*, FSE 2024: asking only
when sampled solutions to the same request disagree improved code generation. *Supports:* the
"materially different readings" test.

**Platform guidance.** OpenAI's Model Spec (2025-12-18) asks models to state assumptions and to
ask only when uncertainty persists after using context; Anthropic's guidance for Claude likewise
discourages unnecessary check-ins on simple tasks. *Supports:* look first, then answer-and-ask
in the same turn.

## 7. Role frameworks and debiasing

Used as shared vocabulary, at the strength shown.

- **Consider the opposite:** Lord, Lepper & Preston (1984), *JPSP* 47(6), 1231–1243, doi.org/10.1037/0022-3514.47.6.1231. Inducing people to consider the opposite corrected biased judgment more than asking them to be unbiased. (Abstract wording via secondary source.)
- **Authentic vs role-played dissent:** Nemeth, Brown & Rogers (2001), *Eur. J. Soc. Psych.* 31(6), 707–720, doi.org/10.1002/ejsp.58. Authentic minority dissent beat all forms of role-played devil's advocate, which tended to bolster the initial view.
- **Devil's advocacy and dialectical inquiry vs consensus:** Schweiger, Sandberg & Ragan (1986), *Academy of Management Journal* 29(1), 51–71. Better recommendations and assumptions than consensus, at the cost of lower satisfaction. (Secondary summaries; primary paywalled.)
- **Feedback aimed at the person:** Kluger & DeNisi (1996), *Psychological Bulletin* 119(2), 254–284, doi.org/10.1037/0033-2909.119.2.254. Over a third of feedback interventions reduced performance, especially when they drew attention to the self rather than the task.
- **Psychological safety:** Edmondson (1999), *Administrative Science Quarterly* 44(2), 350–383. Teams learn when it's safe to speak up and be wrong.
- **Sycophancy at prompt level:** Dubois et al. (UK AISI, 2026), *Ask Don't Tell*, arXiv:2602.23971. Sycophancy is higher for confident statements than questions; converting the user's statement into a question before answering reduced it more than an instruction not to be sycophantic. Laban et al. (2023), *FlipFlop*, arXiv:2311.08596: asked "are you sure?", models flipped about 46% of the time. Hong et al. (2025), *SYCON-Bench*, Findings of EMNLP 2025: a third-person framing reduced sycophancy, up to 63.8% in one scenario (best case, not average).
- **Product:** Cagan (2017), *The Four Big Risks*, svpg.com/four-big-risks: value, usability, feasibility, business viability.
- **Engineering:** Nygard (2011), *Documenting Architecture Decisions*: context, decision, consequences (including negative ones).
- **Hiring:** Sackett, Zhang, Berry & Lievens (2022), *J. Applied Psychology* 107(11), 2040–2068, doi.org/10.1037/apl0000994. Structured interviews rank first (≈ .42), unstructured ≈ .19, cognitive ability ≈ .31; older Schmidt & Hunter (1998) figures were overcorrected.
- **Forecasting:** Kahneman & Lovallo (1993), *Management Science* 39(1), 17–31 (the inside view produces bold forecasts); Flyvbjerg (2006), *Project Management Journal* 37(3), 5–15 (reference-class forecasting).
- **Experiments:** Microsoft Bing (2013), *Large-Scale Experimentation at Bing*: fewer than a third of ideas moved their target metric in controlled experiments.
- **Decision review:** Kahneman, Lovallo & Sibony (2011), *Before You Make That Big Decision…*, HBR 89(6): a 12-question checklist (self-interest, falling in love with the proposal, groupthink, credible alternatives, worst case, ...).
- **Strategy:** Rumelt (2011), *Good Strategy/Bad Strategy*: diagnosis, guiding policy, coherent actions; goals are not strategy. (Book; secondary summaries.)
- **Analysis:** Heuer (1999), *Psychology of Intelligence Analysis*, ch. 8: weight evidence by diagnosticity. An RCT (Dhami, Belton & Mandel, 2019) found the full ACH procedure may increase inconsistency, so use the question, not the ritual.
- **Sales:** MEDDIC is a practitioner checklist; no independent evidence for its claimed win-rate effects.

Full entries with verification status: `research/external-sources.md` in the source repository.

## 8. Myths not to repeat

- **"Premortems improve prediction accuracy by 30%."** Traced to Mitchell, Russo & Pennington
  (1989); the study measured something else (generating reasons with prospective hindsight), and its
  abstract notes that temporal perspective showed little influence. Don't quote the number.
- **"Training removes automation bias."** The review literature says it doesn't (Parasuraman &
  Manzey, 2010).
- **"The AI will tell you if you're wrong."** Not by default; models lean toward agreement. Ask for
  the counter-argument explicitly.
- **"Five users find 85% of usability problems, always."** Nielsen & Landauer's model assumes comparable users and iterative rounds of testing.
- **"Five whys finds the root cause."** It tends to produce a single causal chain; complex failures rarely have one (Card, 2017, *BMJ Quality & Safety*).
- **"Structured interviews have validity .51."** That's the 1998 estimate; current estimates are lower (Sackett et al., 2022).
- **"Two independent BCG studies."** Dell'Acqua et al. (2023) and Randazzo et al. (2025) use the
  same experiment.
