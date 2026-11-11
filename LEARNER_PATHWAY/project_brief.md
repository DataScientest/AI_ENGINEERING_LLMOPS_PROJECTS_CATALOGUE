# Learner Pathway

## Business context

SkillPath Academy supports tech professionals in building their skills. Learning advisors analyze a learner's profile, goal, past results and the available trainings in order to build a tailored pathway.

An advisory interview can take several hours of preparation and discussion. The project aims to assist this work while leaving the decision to the advisor and the learner.

## Users and stakes

The main users are the learning advisors. Learners are the direct recipients of the proposals and can discuss or decline them.

The stakes are to prepare pathways that are relevant, understandable and realistic in terms of prerequisites, duration and availability. The risks concern personal data, bias in recommendations, a proposal that is not sufficiently explainable, and a decision taken in place of the advisor.

## Data provided

The following datasets are provided. They are working sources; which ones you select and the role they play in your proposal are part of the scoping.

- `data/source_documents/data_engineering_profile.md`, `data_scientist_profile.md`, `mlops_profile.md` and `llm_engineer_profile.md`: sheets describing target jobs.
- `data/source_documents/target_roles.md`: overview of the jobs and the skills expected.
- `data/tabular_data/learners.csv`: learner profiles, goals and availability.
- `data/tabular_data/assessments.csv`: results of past assessments.
- `data/tabular_data/training_catalog.csv`: catalog of trainings and their characteristics.
- `data/tabular_data/prerequisites.csv`: prerequisites between trainings or skills.
- `data/tabular_data/certifications.csv`: information about certifications.
- `data/evaluation_sets/eval_recommendations.csv`: reference cases to build and run your evaluation.

## Real-world constraints

- Profiles and assessment results are personal data that must be protected.
- A recommendation must be explainable and allow the advisor to discuss it with the learner.
- Prerequisites, availability and goals can make a proposal unrealistic despite its apparent relevance.
- The final pathway decision belongs to the advisor and the learner; no binding enrollment or change may be automated without human validation.

## Current business workflows

### Prepare a guidance interview

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Request for support → learning advisor, learner → profile, goal, availability and assessment results → identify missing information and plausible goals → prepare the interview questions → focused interview and complete file.

Observable friction and risks: incomplete data, vaguely stated goals, long preparation time.

### Build a pathway proposal

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Interview completed → learning advisor, learner → profile, current skills, trainings, prerequisites, jobs and certifications → choose a goal, a progression order and a realistic workload → present one or more reasoned pathways → understandable, tailored proposal.

Observable friction and risks: forgotten prerequisites, opaque recommendation, bias from historical profiles, unrealistic workload.

### Validate an enrollment or a pathway change

**Trigger → actors → information consulted → decisions → actions → expected outcome**  
Proposal discussed → learner, learning advisor, administration if needed → proposal, schedule constraints, training capacities and the learner's agreement → confirm or adjust the pathway → the human advisor validates the enrollment or change → pathway recorded with the learner's explicit agreement.

Observable friction and risks: a training that is unavailable, poorly tracked consent, a recommendation applied without discussion.

## Your scoping

Based on these elements, choose a priority objective and formulate an observable MVP. Which specific problem deserves to be addressed first, for which user, and why? Define a baseline, a success metric and the sources that are genuinely useful. Specify the level of automation chosen, the risks, the safeguards and the non-goals. Which decision must remain human? What evidence would lead you to conclude that the MVP really helps without increasing risk?

Explicitly justify why a **simple LLM treatment (chat)**, a **Workflow**, a **RAG** or an **Agent** is retained or ruled out for your scope — the simplest solution that proves the value is a legitimate choice. Show how your proposal remains explainable, protects personal data and keeps the decision human.

## Getting started

Start with the [unified AI Engineering methodology](../../AI_engineering_project_message/README.md). It guides you from scoping to operations and recalls the expected software engineering best practices.

Document your important decisions in ADRs and keep the evidence requested at each phase: contract, baseline, tests, evaluation results, traces, and demonstrations of working or controlled-failure behavior.

The set of 5 to 10 cases required from the scoping phase can start from the cases provided in `data/evaluation_sets/`; complete them with your own ambiguous and error cases, documenting what you add and why.
