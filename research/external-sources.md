# External sources: evidence base for `sparring-partner`

Compiled 2026-10-26. Scope: sources NOT in the already-verified set (Bainbridge, Parasuraman & Manzey, Dell'Acqua, Randazzo, Snowden & Boone, Bezos 2015, Klein 2007, Fogliato, Buçinca, Cheng 2026, Bo 2025, Jakesch, Chiang 2024, Lee 2025, Sharma 2023).

**Status legend**
- ✅ verified in primary: the abstract, full text, or official doc page was read directly (arXiv, Crossref, publisher/author-hosted PDF, official docs).
- ⚠️ secondary only: the claim comes from consistent secondary summaries; the primary is paywalled or wasn't readable.
- ❌ couldn't verify.

Numbers are given only where they appear in the source as read. Where a number is commonly misquoted, the entry says so.

---

## 1. Clarifying questions vs. assuming

### 1.1 Aliannejadi, Zamani, Crestani & Croft (2019). *Asking Clarifying Questions in Open-Domain Information-Seeking Conversations.* SIGIR 2019.
- arXiv: https://arxiv.org/abs/1907.06554
- **Says:** Introduces the clarifying-question task and the Qulac dataset. In oracle experiments, "asking only one good question leads to over 170% retrieval performance improvement in terms of P@1."
- **Caveat:** This is an *oracle* upper bound: the best possible question, chosen with hindsight. It shows how much one well-chosen question can be worth, not what a typical question delivers.
- ✅

### 1.2 Zou, Aliannejadi, Kanoulas, Pera & Liu (2023). *Users Meet Clarifying Questions: Toward a Better Understanding of User Interactions for Search Clarification.* ACM TOIS 41(1), Art. 16.
- https://scholarworks.boisestate.edu/cs_facpubs/355
- **Says:** In a user study, high-quality clarifying questions improved user performance and satisfaction. Low- and mid-quality questions were *harmful*, and users did better with no clarification at all. The need for clarification also depended on result quality and perceived task difficulty.
- **Why it matters:** This is the clearest evidence on the cost of asking: a bad question is worse than no question.
- ✅ (abstract)

### 1.3 Rahmani, Wang, Aliannejadi, Naghiaei & Yilmaz (2024). *Clarifying the Path to User Satisfaction: An Investigation into Clarification Usefulness.* EACL 2024 (Findings).
- arXiv: https://arxiv.org/abs/2402.01934
- **Says:** "Specific questions are more effective than generic ones." The subjectivity and emotional tone of a question affect satisfaction. "Shorter and more ambiguous queries benefit significantly from clarification."
- ✅ (abstract)

### 1.4 Kiesel, Bahrami, Stein, Anand & Hagen (2018). *Toward Voice Query Clarification.* SIGIR 2018.
- https://ir.webis.de/anthology/people/j/johannes+kiesel/
- **Says:** Users like being prompted for clarification of ambiguous voice queries, and the overall experience did not get worse when the system asked.
- **Caveat:** Small study with a single clarification turn. It does not license asking many questions.
- ⚠️

### 1.5 Zamani, Mitra, Chen, Lueck, Diaz, Bennett, Craswell & Dumais (2020). *Analyzing and Learning from User Interactions for Search Clarification.* SIGIR 2020.
- arXiv: https://arxiv.org/abs/2006.00166
- **Says:** A large-scale log analysis of how Bing users engage with clarification panes, including position and presentation biases, plus a model that re-ranks clarifying questions from interaction data.
- **Secondary detail (not read in primary):** engagement is higher for more specific questions and for queries with real ambiguity.
- ✅ (abstract) / ⚠️ (detail)

### 1.6 Zhang, T., Qin, P., Deng, Y., et al. (2024). *CLAMBER: A Benchmark of Identifying and Clarifying Ambiguous Information Needs in Large Language Models.* ACL 2024.
- arXiv: https://arxiv.org/abs/2405.12063 · ACL: 2024.acl-long.578
- **Says:** About 12K items built on an ambiguity taxonomy. Current LLMs have limited ability to identify and clarify ambiguous queries. Chain-of-thought and few-shot prompting give only marginal gains and can *increase overconfidence*. LLMs "fall short in generating high-quality clarifying questions due to a lack of conflict resolution and inaccurate utilization of inherent knowledge."
- ✅ (abstract)

### 1.7 Mu, Shi, Wang, Yu, Zhang, Wang, Liu & Wang (2024). *ClarifyGPT: A Framework for Enhancing LLM-based Code Generation via Requirements Clarification.* FSE 2024.
- arXiv: https://arxiv.org/abs/2310.10996 · DOI: 10.1145/3660810
- **Says:** The framework asks *only when* a consistency check finds the requirement ambiguous: it samples several solutions, runs them on generated test inputs, and treats divergent outputs as a sign of ambiguity. In a human evaluation, GPT-4 Pass@1 on MBPP-sanitized rose from 70.96% to 80.80%.
- **Caveat:** The aggregate benchmark numbers differ between arXiv versions; quote only the human-evaluation figure.
- **Key design idea:** gate questions on detected divergence of interpretations, not on "the request is vague in general."
- ✅

### 1.8 Zhang, M. J. Q. & Choi, E. (2023/2025). *Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs.* Findings of NAACL 2025.
- arXiv: https://arxiv.org/abs/2311.09469
- **Says:** Splits clarification into three subtasks: (1) whether to ask, (2) what to ask, and (3) how to answer using the reply. It proposes INTENT-SIM, which estimates entropy over plausible user intents, to decide when a question is worth asking.
- ✅ (abstract)

### 1.9 Zhang, M. J. Q., Knox, W. B. & Choi, E. (2025). *Modeling Future Conversation Turns to Teach LLMs to Ask Clarifying Questions.* ICLR 2025.
- arXiv: https://arxiv.org/abs/2410.13788
- **Says:** LLMs tend to presuppose a single interpretation of an ambiguous request. The authors attribute this to preference labels that judge only the immediate response. Training on simulated future turns improved F1 against the set of valid interpretations by 5%.
- ✅ (abstract)

### 1.10 Luo et al. (2025). *ClarifyMT-Bench: Benchmarking and Improving Multi-Turn Clarification for Conversational LLMs.*
- arXiv: https://arxiv.org/abs/2512.21120
- **Says:** 6,120 multi-turn dialogues across five ambiguity dimensions and six user personas. It finds a consistent "under-clarification bias": LLMs answer too early, and this gets worse as the dialogue gets longer.
- ✅ (abstract)

### 1.11 OpenAI Model Spec (version 2025-12-18). Section "Consider uncertainty, state assumptions, and ask clarifying questions when appropriate."
- https://model-spec.openai.com/2025-12-18.html
- **Says (verbatim excerpts):**
  - "weigh the cost of incorrect assumptions against the inconvenience of asking the user"
  - "attempt to fill information gaps using context or trusted external sources … resorting to direct user queries only when uncertainty persists"
  - "Unless the cost of making the wrong assumption is too high or the task is too ambiguous … the assistant typically should take a stab at fulfilling the request and tell the user that it could be more helpful with certain information"
  - "asking clarifying questions and proceeding with preliminary actions should happen concurrently"
  - Elsewhere: assume reasonable-human goals, "avoiding unnecessary or trivial clarifying questions"
- **Worked example:** the "Rochester" query is marked compliant when the assistant answers the dominant reading and offers the alternative. Asking only "Do you mean NY or MN?" is marked a *violation*.
- ✅

### 1.12 Anthropic, *Claude's Constitution* (2026).
- https://www.anthropic.com/constitution
- **Says:**
  - "Claude should ask for clarification in cases of genuine ambiguity."
  - Claude also shouldn't "make too many of its own assumptions about what the user 'really' wants beyond what is reasonable."
  - Among behaviours a thoughtful senior employee would dislike: "Checks in or asks clarifying questions more than necessary for simple agentic tasks."
- ✅

### 1.13 Anthropic, *Prompting best practices* (Claude docs).
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **Says:** Gives two ready-made system-prompt snippets:
  - `<default_to_action>`: "infer the most useful likely action and proceed, using tools to discover any missing details instead of guessing"
  - `<do_not_act_before_instructions>`: when intent is ambiguous, default to information and recommendations
- **Also says:**
  - Recent models are more responsive to the system prompt. Aggressive wording ("CRITICAL: You MUST…") can cause overtriggering, so soften it.
  - Explaining *why* an instruction exists improves compliance.
- ✅

---

## 2. Sycophancy: what reduces it at prompt level

### 2.1 Dubois, Ududec, Summerfield & Luettgau (UK AISI) (2026). *Ask Don't Tell: Reducing Sycophancy in Large Language Models.*
- arXiv: https://arxiv.org/abs/2602.23971
- **Says:** A factorial study of input framing. Sycophancy is substantially higher when the user makes a *statement* than when they ask a *question*. It rises monotonically with the user's expressed certainty and is amplified by first-person framing. Asking the model to *convert the user's statement into a question before answering* reduced sycophancy more than simply instructing it "not to be sycophantic."
- ✅ (abstract)

### 2.2 Hong, Byun, Kim, Shu & Choi (2025). *Measuring Sycophancy of Language Models in Multi-turn Dialogues (SYCON-Bench).* Findings of EMNLP 2025, pp. 2239–2259.
- arXiv: https://arxiv.org/abs/2505.23840
- **Says:**
  - Measures "Turn of Flip" and "Number of Flip" under sustained user pressure across 17 LLMs.
  - Alignment tuning *amplifies* sycophancy, while scaling and reasoning optimisation reduce it.
  - Reasoning models can still fail by over-indexing on logical exposition instead of engaging the user's actual belief.
  - Of the prompting strategies tested, a third-person perspective reduced sycophancy "by up to 63.8% in debate scenario."
- **Caveat:** The 63.8% is a best case in one scenario, not an average.
- ✅ (abstract)

### 2.3 Laban, Murakhovs'ka, Xiong & Wu (2023). *Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment.*
- arXiv: https://arxiv.org/abs/2311.08596
- **Says:** When challenged with "Are you sure?", ten LLMs on seven classification tasks flipped their answer 46% of the time on average, with an average 17% accuracy drop. Fine-tuning on synthetic data reduced the deterioration by about 60% but did not eliminate it.
- **Relevance:** The model should hold its position unless the user gives a new argument or new evidence. Pushback alone is not a reason to fold.
- ✅ (abstract)

### 2.4 OpenAI Model Spec (2025-12-18), "Don't be sycophantic."
- https://model-spec.openai.com/2025-12-18.html
- **Says:**
  - "the factual aspects of the assistant's response should not differ based on how the user's question is phrased"
  - The assistant "should not change its stance solely to agree with the user"
  - When asked to critique, it should be "a firm sounding board … rather than a sponge that doles out praise"
- ✅

### 2.5 Anthropic, *Claude's Constitution* (2026), honesty section.
- https://www.anthropic.com/constitution
- **Says:**
  - "Claude should be diplomatically honest rather than dishonestly diplomatic."
  - "Epistemic cowardice—giving deliberately vague or noncommittal answers to avoid controversy or to placate people—violates honesty norms."
  - Claude should "engage critically with speculative ideas rather than giving empty validation."
- ✅

---

## 3. Structured challenge techniques

### 3.1 Schweiger, Sandberg & Ragan (1986). *Group Approaches for Improving Strategic Decision Making: A Comparative Analysis of Dialectical Inquiry, Devil's Advocacy, and Consensus.* Academy of Management Journal 29(1), 51–71.
- DOI: 10.5465/255859
- **Says:** In the lab, both dialectical inquiry (DI) and devil's advocacy (DA) produced higher-quality recommendations and assumptions than consensus. Consensus groups reported *more satisfaction, more decision acceptance and more desire to keep working together*.
- **Takeaway:** Challenge improves decision quality but costs affect.
- **Follow-up:** Schweiger, Sandberg & Rechner (1989), AMJ, DOI 10.5465/256567, found that experience with the methods reduced these costs.
- ⚠️ (AOM paywalled. The finding is consistent across several secondary summaries, but the abstract was not read directly.)

### 3.2 Schwenk (1990). *Effects of Devil's Advocacy and Dialectical Inquiry on Decision Making: A Meta-Analysis.* OBHDP 47(1), 161–176.
- DOI: 10.1016/0749-5978(90)90051-A
- **Says:** Both DA and DI improve decisions compared with expert-based, non-conflictual approaches.
- **Caveat:** Effect sizes and the DA-vs-DI comparison were not verified. Don't quote numbers.
- ⚠️ (metadata verified via Crossref; abstract not available)

### 3.3 Nemeth, Brown & Rogers (2001). *Devil's Advocate versus Authentic Dissent: Stimulating Quantity and Quality.* European Journal of Social Psychology 31(6), 707–720.
- DOI: 10.1002/ejsp.58
- **Says:** Role-played devil's advocacy tended to trigger "cognitive bolstering of the initial viewpoint." The "authentic minority was superior to all three forms of 'devil's advocate'," which shows "the difficulty in cloning such authenticity by role-playing techniques."
- **Key implication for an AI sparring partner:** a performative "let me play devil's advocate" is weaker than a challenge the AI actually holds and can justify.
- ✅ (abstract via Crossref)

### 3.4 Lord, Lepper & Preston (1984). *Considering the Opposite: A Corrective Strategy for Social Judgment.* JPSP 47(6), 1231–1243.
- DOI: 10.1037/0022-3514.47.6.1231
- **Says:** In two experiments (biased assimilation of evidence, and biased hypothesis testing), inducing people to *consider the opposite* corrected bias more than instructions to "be as fair and unbiased as possible."
- **Takeaway:** Generic exhortations to be unbiased are weak. A concrete counter-scenario works better.
- ⚠️ (Crossref metadata verified; the abstract wording comes from a secondary mirror because APA PsycNet is paywalled)

### 3.5 Mitchell, Russo & Pennington (1989). *Back to the Future: Temporal Perspective in the Explanation of Events.* Journal of Behavioral Decision Making 2(1), 25–38.
- DOI: 10.1002/bdm.3960020103
- **What the abstract actually says:** "temporal perspective showed little influence while outcome uncertainty strongly affected the nature of explanations." Explanations for *certain* events were longer, more episodic and in past tense.
- **The 30% myth:** Klein (2007) wrote that prospective hindsight "increases the ability to correctly identify reasons for future outcomes by 30%." The study measured the *number and type* of reasons generated, not whether they were correct, and the effect came from framing the outcome as certain, not from the future/past perspective.
- **Safe phrasing:** "imagining the failure as certain tends to produce more, and more concrete, failure explanations."
- ✅ (abstract via Crossref). The misquote is also documented by Jason Collins: https://corporate.jcx.au/premortem ⚠️

### 3.6 Veinott, Klein & Wiggins (2010). *Evaluating the Effectiveness of the PreMortem Technique on Plan Confidence.* Proceedings of ISCRAM 2010.
- **Says:** 178 students evaluated an H1N1 response plan under five conditions. The premortem reduced (over)confidence more than pro/con or cons-only critique.
- **Caveat:** The measured outcome is *confidence*, not decision quality or plan accuracy.
- ⚠️ (proceedings PDF not retrieved)

### 3.7 Edmondson (1999). *Psychological Safety and Learning Behavior in Work Teams.* Administrative Science Quarterly 44(2), 350–383.
- DOI: 10.2307/2666999
- **Says:**
  - Defines team psychological safety as "a shared belief … that the team is safe for interpersonal risk taking."
  - In 51 manufacturing teams it was associated with learning behaviour, and learning behaviour mediated its effect on performance. Team efficacy was not associated with learning once psychological safety was controlled for.
- **Follow-up review:** Edmondson & Lei (2014), Annual Review of Organizational Psychology and Organizational Behavior (2014); volume and pages not verified.
- ✅ (abstract via Crossref)

### 3.8 Kluger & DeNisi (1996). *The Effects of Feedback Interventions on Performance: A Historical Review, a Meta-Analysis, and a Preliminary Feedback Intervention Theory.* Psychological Bulletin 119(2), 254–284.
- DOI: 10.1037/0033-2909.119.2.254
- **Says:** 607 effect sizes and 23,663 observations. Feedback improved performance on average (d = .41), but "over 1/3 of the FIs decreased performance." Effectiveness "decreases as attention moves up the hierarchy closer to the self and away from the task."
- **Takeaway:** Critique aimed at the person backfires. Critique aimed at the task works.
- ✅ (author-hosted abstract, pluto.huji.ac.il)

### 3.9 UK Ministry of Defence, DCDC (2021). *Red Teaming Handbook*, 3rd ed.
- https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1027158/20210625-Red_Teaming_Handbook.pdf
- **Definition:** Red teaming is "the independent application of a range of structured, creative and critical thinking techniques to assist the end user make a better-informed decision or produce a more robust product."
- **Guidance on delivery:**
  - The devil's advocate must not be "too adversarial in tone," and criticism should not be "given or taken personally."
  - The role must not be "paid 'lip service'," because a sham challenge "can instil more confidence in the plan because it has apparently been tested, when in reality it has not."
  - Findings must be "fair, justifiable, non-personal, constructive and honest," but the red team must not "shy away from telling the hard truths."
  - "Set a clear objective – the red team needs to know which question it is answering."
  - Red teams can be "resented and mistrusted."
- ✅

### 3.10 Dennett (2013). *Intuition Pumps and Other Tools for Thinking* (W. W. Norton). "Rapoport's Rules."
- **Says:** Before criticising: (1) re-express the target's position "so clearly, vividly, and fairly that your target says, 'Thanks, I wish I'd thought of putting it that way'"; (2) list points of agreement; (3) mention anything you learned from the target; (4) only then rebut. This is the canonical source for "steelmanning."
- **Evidence status:** A normative rule from philosophy, not an experimental finding. No RCT evidence was found that steelmanning improves decisions.
- ⚠️ (book; quote consistent across many secondary sources)

### 3.11 Braun, Strunk, Sasso & Cooper (2015). *Therapist Use of Socratic Questioning Predicts Session-to-Session Symptom Change in Cognitive Therapy for Depression.* Behaviour Research and Therapy 70, 32–37.
- DOI: 10.1016/j.brat.2015.05.004 · PMC4449800
- **Says:** In 55 patients, a within-patient 1 SD increase in Socratic questioning predicted a 1.51-point BDI-II drop in the next session, independent of therapeutic alliance. The authors note causal claims would need experimental manipulation.
- **Relevance:** This is the best quantitative evidence for Socratic questioning, but it comes from therapy, not workplace decisions. Use it as an analogy, not as proof.
- ✅

### 3.12 Card (2017). *The Problem with '5 Whys'.* BMJ Quality & Safety 26(8), 671–677.
- DOI: 10.1136/bmjqs-2016-005849
- **Says:** "5 whys" is useful as a teaching tool. Used for root-cause analysis, it oversimplifies: it follows a single causal chain to a single root cause when failures are multi-causal, and it limits understanding of how processes fail. Card recommends fishbone- or lovebug-style multi-cause tools instead.
- ⚠️ (Crossref metadata ✅; argument via the AHRQ PSNet summary because BMJ returned 403)

### 3.13 Vogels (2006). *Working Backwards.* All Things Distributed (Amazon CTO blog).
- https://www.allthingsdistributed.com/2006/11/working_backwards.html
- **Says:** Write the press release first, then the FAQ, then a customer-experience description, then the user manual. "You start with your customer and work your way backwards until you get to the minimum set of technology requirements."
- **Further reading:** Bryar & Carr (2021), *Working Backwards*, St. Martin's Press, for the PR/FAQ in its mature form.
- ✅ (Vogels) / ⚠️ (Bryar & Carr not read)

### 3.14 Kahneman, Lovallo & Sibony (2011). *Before You Make That Big Decision…* Harvard Business Review 89(6), June 2011.
- https://store.hbr.org/product/the-big-idea-before-you-make-that-big-decision/R1106B
- **Says:** A 12-question checklist for the *decision-maker reviewing a team's proposal*:
  1. Self-interest / motivated errors?
  2. Has the team fallen in love with it?
  3. Were dissenting opinions explored?
  4. Salient analogies?
  5. Credible alternatives?
  6. What information would you want in a year, and can you get it now?
  7. Where did the numbers come from?
  8. Halo effect?
  9. Attachment to past decisions?
  10. Is the base case overly optimistic?
  11. Is the worst case bad enough?
  12. Is the team overly cautious?
- **Caveat:** A practitioner checklist, not experimentally validated.
- ✅ (full text, university-hosted copy)

---

## 4. Anthropic guidance on writing Agent Skills

### 4.1 Anthropic, *Skill authoring best practices.*
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- **Frontmatter:**
  - `name`: at most 64 characters; lowercase letters, numbers and hyphens; no XML tags; no "anthropic" or "claude".
  - `description`: non-empty, at most 1,024 characters, no XML; must say *what the Skill does and when to use it*.
  - **Write the description in third person**, because it is injected into the system prompt.
  - Include specific trigger terms. Claude picks from "potentially 100+ available Skills" using the description.
- **Conciseness:** "The context window is a public good." Default assumption: "Claude is already very smart." Only add context Claude doesn't already have.
- **Body length:** "Keep the SKILL.md body under 500 lines"; split into files when approaching the limit.
- **Progressive disclosure:**
  - Only name and description are preloaded. SKILL.md loads when the Skill triggers, and other files load only when read.
  - Keep reference files *one level deep* from SKILL.md; nested references get partially read with `head`.
  - Give reference files over 100 lines a table of contents.
  - Organise by domain, e.g. `reference/finance.md` and `reference/sales.md`. That fits per-role challenge packs.
- **Degrees of freedom:** Use high freedom (heuristics) when "decisions depend on context." This fits a sparring partner.
- **Other content rules:**
  - Avoid time-sensitive information.
  - Use consistent terminology.
  - Provide a default rather than many options.
  - Give concrete examples.
  - Use checklists and feedback loops for multi-step workflows.
- **Evaluation:** "Create evaluations BEFORE writing extensive documentation." Build at least 3 evaluation scenarios, compare against a no-Skill baseline, and test with Haiku, Sonnet and Opus. Iterate with a "Claude A" that writes the Skill and a "Claude B" that uses it.
- ✅

### 4.2 Claude Code docs, *Skills.*
- https://code.claude.com/docs/en/skills
- **Claude Code-specific frontmatter:** `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`, `agent`, `hooks`, `paths`, `argument-hint`, `when_to_use`.
- **Locations:** `~/.claude/skills/<name>/SKILL.md` (personal), `.claude/skills/<name>/SKILL.md` (project), and plugins.
- **Listing limit:** The combined `description` + `when_to_use` is **truncated at 1,536 characters** in the skill listing. "Put the key use case first."
- **Body length:** "Keep SKILL.md under 500 lines."
- ✅

### 4.3 Anthropic, *Prompting best practices*: wording intensity.
- See 1.13.
- **Says:** Avoid "CRITICAL/MUST" shouting on current models, because it causes overtriggering. Explain the reason behind a rule instead.
- ✅

---

## 5. Role-specific challenge frameworks (1–2 per function)

### Product: Cagan (2017). *The Four Big Risks.* SVPG, 4 Dec 2017.
- https://svpg.com/four-big-risks/
- **Value risk:** "whether customers will buy it or users will choose to use it"
- **Usability risk:** "whether users can figure out how to use it"
- **Feasibility risk:** "whether our engineers can build what we need with the time, skills and technology we have"
- **Business viability risk:** "whether this solution also works for the various aspects of our business" (go-to-market, legal, acquisition cost, monetisation, brand)
- ✅

### Product / discovery: Torres, *Opportunity Solution Tree.* Product Talk.
- https://www.producttalk.org/glossary-discovery-opportunity-solution-tree/
- **Says:** Four levels: Desired Outcome → Opportunity Space (customer needs, pain points, desires) → Solution Space → Assumption Tests.
- **Challenge it enables:** Is this a solution looking for an opportunity? Which assumption is untested?
- ✅

### Engineering: Nygard (2011). *Documenting Architecture Decisions.* Cognitect blog, 15 Nov 2011.
- https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Says:** The Architecture Decision Record has five sections: Title, Context ("forces at play"), Decision, Status, Consequences. "All consequences should be listed here, not just the 'positive' ones."
- **Challenge it enables:** What are the forces, and what are the negative consequences?
- ✅

### Design / UX research: Nielsen & Landauer (1993). *A Mathematical Model of the Finding of Usability Problems.* CHI '93, 206–213.
- DOI: 10.1145/169059.169166
- Popularised in Nielsen (2000), *Why You Only Need to Test with 5 Users*: https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- **Says:** About 85% of problems are found with 5 users, *assuming* a per-user discovery rate L ≈ 31% and comparable users. Nielsen recommends several small iterative rounds rather than one big test, and more users when there are distinct user groups.
- **Common misquote:** "5 users is always enough." The caveats above are in Nielsen's own article.
- ✅ (NN/g article); CHI paper metadata via Crossref

### Sales: MEDDIC (Metrics, Economic buyer, Decision criteria, Decision process, Identify pain, Champion).
- **Origin:** Attributed to Dick Dunkel and Jack Napoli, with John McMahon, at PTC around 1996.
- **Book:** Whyte, A. (2020), *MEDDICC: The Ultimate Guide to Staying One Step Ahead in the Complex Sale.*
- **Caveat:** No peer-reviewed validation was found. Win-rate claims such as "mid-teens to high twenties" or "25–30% higher close rates" come from vendor and blog sources. Do not cite them as evidence.
- ⚠️ (framework content) / ❌ (any effectiveness numbers)

### Finance / forecasting
- **Kahneman & Lovallo (1993).** *Timid Choices and Bold Forecasts: A Cognitive Perspective on Risk Taking.* Management Science 39(1), 17–31. DOI 10.1287/mnsc.39.1.17.
  - **Says:** Decision makers treat problems as unique and "neglect the statistics of the past." "Overly optimistic forecasts result from the adoption of an inside view."
  - ✅ (abstract via Crossref)
- **Flyvbjerg (2006).** *From Nobel Prize to Project Management: Getting Risks Right.* Project Management Journal 37(3), 5–15. DOI 10.1177/875697280603700302.
  - **Says:** Attributes forecast inaccuracy to optimism bias *and strategic misrepresentation*. Reference class forecasting bases forecasts "on actual performance in a reference class of comparable projects."
  - ✅ (abstract via Crossref)
- **Challenge it enables:** What is the base rate for projects like this one?

### Marketing / growth: experiment design
- **Kohavi, Longbotham, Sommerfield & Henne (2009).** *Controlled Experiments on the Web: Survey and Practical Guide.* Data Mining and Knowledge Discovery 18(1), 140–181. DOI 10.1007/s10618-008-0114-1.
  - Metadata ✅ via Crossref; content not re-read ⚠️.
- **Microsoft Bing blog (2013).** *Large-Scale Experimentation at Bing.*
  - https://blogs.bing.com/search-quality-insights/August-2013/Large-Scale-Experimentation-at-Bing
  - **Says:** "When ideas are evaluated objectively in a controlled experiment, less than a third move the metrics they were designed to improve," and fewer still in an optimised domain like Bing.
  - ✅
- **Challenge it enables:** What is the falsifiable hypothesis, the primary metric and the prior that this idea works?

### HR / hiring: structured interviews
- **Schmidt & Hunter (1998).** *The Validity and Utility of Selection Methods in Personnel Psychology.* Psychological Bulletin 124(2), 262–274. DOI 10.1037/0033-2909.124.2.262.
  - **Says:** Tabled validities of .51 for structured interviews, .38 for unstructured interviews and .51 for general mental ability (GMA).
  - ✅ (values as quoted by Sackett et al. 2022)
- **Sackett, Zhang, Berry & Lievens (2022).** *Revisiting Meta-Analytic Estimates of Validity in Personnel Selection.* Journal of Applied Psychology 107(11), 2040–2068. DOI 10.1037/apl0000994.
  - **Says:** Earlier range-restriction corrections overcorrected, so most validities fall by .10–.20. Structured interviews are the **top-ranked** procedure (about .42), unstructured interviews about .19, and cognitive ability tests about .31.
  - ✅ (full text)
- **Caveat:** Schmidt & Hunter (1998) is outdated on magnitudes. Cite Sackett et al. (2022) for current numbers.

### Strategy / leadership: Rumelt (2011). *Good Strategy/Bad Strategy* (Crown Business). Also McKinsey Quarterly (2011), "The perils of bad strategy."
- **Says:** The "kernel" of a strategy is a diagnosis, a guiding policy and coherent actions. The hallmarks of bad strategy are fluff, failure to face the challenge, mistaking goals for strategy, and bad strategic objectives.
- **Challenge it enables:** What is the diagnosis? Is this a goal masquerading as a strategy?
- ⚠️ (book; the McKinsey page timed out; consistent across secondary summaries)
- **For leadership decision review,** also use Kahneman, Lovallo & Sibony (2011), entry 3.14 ✅.

### Analysts / intelligence-style reasoning: Heuer (1999). *Psychology of Intelligence Analysis*, Ch. 8, "Analysis of Competing Hypotheses." CIA Center for the Study of Intelligence.
- https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf
- **Says:** Lay out all competing hypotheses and look for evidence that *refutes* them, rather than confirms the favourite. Weight evidence by its *diagnosticity*: "If an item of evidence seems consistent with all the hypotheses, it may have no diagnostic value at all."
- ✅
- **Counter-evidence:** Dhami, Belton & Mandel (2019), *The "analysis of competing hypotheses" in intelligence analysis*, Applied Cognitive Psychology. In an RCT with 50 analysts, ACH users did not follow all the steps, the evidence that ACH reduces confirmation bias was mixed, and ACH "may increase judgment inconsistency and error."
  - https://strathprints.strath.ac.uk/69049/ ⚠️ (abstract via repository summary)
  - **Implication:** Use the diagnosticity question, not the full ACH ritual.

### Legal / ops / risk
- No single strong function-specific framework was verified.
- Use the premortem framing (3.5 and 3.6, with their caveats), red-team principles (3.9), and the "Is the worst case bad enough?" question from Kahneman et al. (3.14). The "5 whys" caveats (3.12) apply to incident reviews.

---

## Implications for the skill design

1. **Ask few questions, only when the answer would change the critique.** Asking is justified when plausible interpretations diverge in a way that would change the attack (ClarifyGPT's consistency check; INTENT-SIM's entropy over intents). Low- and mid-quality questions are *worse than none* (Zou et al. 2023). Cap at about 1–3 sharp, specific questions per turn (Rahmani et al. 2024: specific beats generic).
2. **Default to "answer and ask" in the same turn.** Both the Model Spec and the Anthropic Constitution penalise unnecessary questions. Pattern: "Assuming X, here are the three weakest points… If it's actually Y, point 2 changes. Which is it?" State the assumption explicitly. Use clarify-only turns only when no useful critique is possible.
3. **Fill gaps from context before asking.** Read the provided docs, repo and conversation before asking anything (Model Spec: ask the user "only when uncertainty persists"). Never ask what the artifact already answers.
4. **Fight the under-clarification bias on high-stakes ambiguity.** LLMs tend to assume a single interpretation (CLAMBER; ClarifyMT-Bench; Zhang et al. 2025). The skill should explicitly check for ambiguity in goals, success metrics, constraints and audience before attacking a plan.
5. **Reframe statements as questions internally to resist sycophancy.** Tell the model to rephrase the user's confident claim ("X will work") as a question ("Will X work?") before evaluating it. This beat a bare "don't be sycophantic" instruction (Dubois et al. 2026). A third-person framing ("evaluate this proposal from a colleague") helps too (SYCON-Bench).
6. **Hold position under pushback unless given new evidence or a new argument.** Models flip about 46% of the time on "are you sure?" (FlipFlop). The skill should name what would change its mind, and concede explicitly when that bar is met.
7. **Make the challenge authentic, not role-played.** Nemeth et al. (2001) found authentic dissent beats devil's-advocate role-play, and the MoD warns that sham challenge *raises* false confidence. Ground every objection in a specific reason, rank by severity, and say "I don't see a serious problem with X" when there isn't one. Don't manufacture objections.
8. **Steelman first, then attack.** Open with a one-to-two-line restatement the user would accept (Rapoport's Rules), then the critique. This cuts strawmanning and makes the critique easier to accept.
9. **Attack the task, never the self.** Feedback aimed at the person reduces performance (Kluger & DeNisi 1996: over a third of feedback interventions hurt). Keep tone "non-personal, constructive and honest" (MoD), and keep psychological safety intact (Edmondson 1999). Expect some dissatisfaction as the price of quality (Schweiger et al. 1986). Don't optimise for the user feeling good.
10. **Use specific counterfactuals, not exhortation.** "Consider the opposite" beats "be unbiased" (Lord et al. 1984). Use dialectical moves: give the strongest alternative plan, ask for the base rate (Kahneman & Lovallo 1993; Flyvbjerg 2006), and ask what evidence would discriminate between hypotheses (Heuer's diagnosticity).
11. **Cite techniques honestly.**
    - Premortem: frame failure as certain. It yields more and more concrete reasons and lowers overconfidence. Don't say it is "30% more accurate."
    - 5 whys: warn about single-cause chains.
    - ACH: use the diagnosticity question, not the full ritual.
    - 5-user testing: state the assumptions behind it.
    - MEDDIC: a checklist, not proven science.
12. **Package as SKILL.md plus per-role reference files.** Keep a short core: the protocol (steelman → assumptions → top risks → questions → what would change my mind). Put the role lenses in `reference/<role>.md`, one level deep, each with a TOC if over 100 lines. Keep the body under 500 lines. Write a third-person description that names the trigger words and roles, put the key use case first (the listing truncates at 1,536 characters), use calm wording rather than "MUST" shouting, and build at least 3 evals against a no-skill baseline before expanding.
