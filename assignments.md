# LangChain Single-Agent Assignments

## Overview

You have been given a working LangChain agent project — **Email Humanizer** — as your reference implementation. Your task is to **build your own unique use case** using the exact same framework and patterns.

Study the `email_humanizer_agent.py` file carefully. Your agent must follow the same structure:

```
[User Input] --> [Tool 1] --> [Tool 2] --> [Final Output]
```

Each student below has been assigned their **own unique agent**. Build the one next to your name — do not swap or copy another student's use case.

---

## What You Must Build

Using the same LangChain patterns from the reference code:

- `ChatOpenAI` — the LLM
- `PromptTemplate` — to shape LLM responses
- `@tool` decorator — to define at least 2 tools
- `create_agent` — to wire everything together
- A `SYSTEM_PROMPT` — to define agent behaviour
- A `run_<your_agent>()` function — as the main entry point
- A simple CLI loop in `main()` — so anyone can run and try your agent

---

## Submission Steps

1. **Fork or clone** this repo to your local machine
2. **Create your own Python file** (e.g., `debate_coach_agent.py`) — do NOT modify `email_humanizer_agent.py`
3. **Build your use case** following the same structure
4. **Test it** — make sure it runs end-to-end with your OpenAI key
5. **Push your code** to a **new public GitHub repository** under your own account
6. **Share the GitHub link** in the Excel sheet shared on WhatsApp

Your repo must contain:
- Your agent `.py` file
- A `requirements.txt`
- A `.env.example` file (never commit your real `.env`)
- A `README.md` explaining what your agent does and how to run it

---

## Individual Assignments

---

### 1. Srinath Sreedharan — Article Simplifier Agent

**Use Case:** A user pastes a long news article or technical write-up. The agent first produces a concise summary, then re-explains it in ultra-simple language anyone can understand.

**Tool 1 — `summarize_article`**
- Input: the full article text
- Task: Condense the article into a tight summary capturing the key facts, arguments, and conclusions
- Output: A 4–6 sentence summary plus a one-line headline

**Tool 2 — `explain_like_im_ten`**
- Input: the summary from Tool 1
- Task: Rewrite the summary in extremely simple language — short sentences, everyday words, a relatable analogy — as if explaining to a 10-year-old
- Output: A plain, jargon-free explanation with one helpful analogy

**System Prompt:** The agent acts as a friendly news explainer who makes any article understandable to absolutely anyone.

---

### 2. Sharath R N — Commit Message & Changelog Agent

**Use Case:** A developer pastes a raw git diff or a rough description of code changes. The agent analyses what changed and then writes a clean commit message and a changelog entry.

**Tool 1 — `analyze_code_changes`**
- Input: a git diff or a rough description of the changes
- Task: Identify what was added, removed, or modified, the intent behind the change, and whether it's a feature, fix, refactor, or docs change
- Output: A structured change analysis with change type and affected areas

**Tool 2 — `write_commit_and_changelog`**
- Input: the change analysis from Tool 1
- Task: Write a conventional commit message (type, short subject, descriptive body) and a user-facing changelog entry
- Output: A ready-to-use commit message plus a one-paragraph changelog entry

**System Prompt:** The agent acts as a meticulous senior developer who writes commit histories other engineers love to read.

---

### 3. Rituparna Hazra — Blog Post Writer Agent

**Use Case:** A user provides a blog topic and target keywords. The agent creates an SEO-friendly outline and then expands it into a complete blog post.

**Tool 1 — `create_blog_outline`**
- Input: blog topic, target audience, and 2–3 keywords to rank for
- Task: Structure the post with an attention-grabbing title, introduction angle, H2/H3 section headings, and a conclusion with call-to-action — weaving the keywords in naturally
- Output: A complete blog outline with title options and section headings

**Tool 2 — `write_blog_post`**
- Input: the outline from Tool 1
- Task: Expand the outline into a full 600–800 word blog post with a hook opening, smooth transitions, and a closing call-to-action
- Output: The finished blog post in Markdown

**System Prompt:** The agent acts as a professional content writer who turns any topic into an engaging, SEO-aware blog post.

---

### 4. Suganya Krishnasamy — Plant Care Advisor Agent

**Use Case:** A user describes a plant they own and the problems it's showing (yellow leaves, drooping, spots), along with its living conditions. The agent diagnoses what's wrong and then builds a week-by-week care and recovery plan.

**Tool 1 — `diagnose_plant_health`**
- Input: plant type, visible symptoms, and current conditions (light, watering frequency, indoor/outdoor, pot size)
- Task: Identify the most likely causes of the symptoms (overwatering, low light, pests, nutrient deficiency), ranked from most to least probable, with reasoning for each
- Output: A ranked diagnosis with the most likely cause highlighted

**Tool 2 — `create_care_plan`**
- Input: the diagnosis from Tool 1 + the plant type
- Task: Build a 4-week recovery and care schedule — watering frequency, light placement, feeding, pruning/repotting steps — plus warning signs to watch for
- Output: A week-by-week care plan with a short "signs it's recovering" checklist

**System Prompt:** The agent acts as a friendly houseplant expert who helps plant owners figure out what's wrong and nurse their plants back to health.

---

### 5. Karthika S — FAQ Generator Agent

**Use Case:** A user pastes a product or service description. The agent anticipates the questions real customers would ask and then writes clear, friendly FAQ answers.

**Tool 1 — `anticipate_customer_questions`**
- Input: a product or service description
- Task: Predict the 8–10 most likely customer questions — covering pricing, usage, compatibility, returns/support, and common doubts
- Output: A numbered list of realistic customer questions grouped by theme

**Tool 2 — `write_faq_answers`**
- Input: the questions from Tool 1 + the original product description
- Task: Write a clear, honest, friendly answer for each question (2–4 sentences each), admitting openly when something isn't covered by the description
- Output: A complete FAQ section ready to publish on a website

**System Prompt:** The agent acts as a customer support lead who knows exactly what customers will ask before they ask it.

---

### 6. Prem K Sundar — Debate Coach Agent

**Use Case:** A user provides a debate topic and which side they must argue. The agent builds their strongest arguments and then prepares them for the opponent's attacks.

**Tool 1 — `build_arguments`**
- Input: the debate topic and the side to argue (for / against)
- Task: Construct the 4–5 strongest arguments for that side, each with supporting reasoning and an example
- Output: A numbered list of arguments, strongest first, each with reasoning and an example

**Tool 2 — `prepare_rebuttals`**
- Input: the topic, the user's side, and the arguments from Tool 1
- Task: Predict the opponent's most likely counter-arguments and write a sharp rebuttal for each
- Output: A list of anticipated attacks, each paired with a ready-to-deliver rebuttal

**System Prompt:** The agent acts as a championship debate coach who prepares students to argue any side persuasively and stay unshaken under fire.

---

### 7. Sajjan Kanjaguli — Trip Packing Assistant Agent

**Use Case:** A user shares their destination, travel dates/season, trip length, and planned activities. The agent analyses what the trip demands and then produces a complete packing checklist.

**Tool 1 — `analyze_trip_needs`**
- Input: destination, season or travel dates, trip duration, and planned activities (e.g., trekking, business meetings, beach)
- Task: Work out the expected weather, cultural dress considerations, and activity-specific gear needs
- Output: A trip-needs profile covering climate, dress code notes, and special equipment required

**Tool 2 — `create_packing_checklist`**
- Input: the trip-needs profile from Tool 1
- Task: Build a categorised packing checklist (clothing, toiletries, documents, electronics, activity gear) with quantities based on trip length
- Output: A complete checklist with quantities, plus a short "don't forget" list of commonly missed items

**System Prompt:** The agent acts as a seasoned traveller who makes sure users never overpack or leave essentials behind.

---

### 8. Vivek Jadhav — User Story Generator Agent

**Use Case:** A user describes a product feature idea in plain language. The agent converts it into proper agile user stories and then writes testable acceptance criteria for each.

**Tool 1 — `write_user_stories`**
- Input: a feature idea in plain language (e.g., "let users reset their password by email")
- Task: Break the feature into 2–4 user stories in the standard format: "As a [role], I want [action], so that [benefit]" — covering the main flow and important variations
- Output: A numbered list of well-formed user stories

**Tool 2 — `generate_acceptance_criteria`**
- Input: the user stories from Tool 1
- Task: Write clear, testable acceptance criteria for each story using Given / When / Then format, including at least one edge case per story
- Output: Each story followed by its acceptance criteria in Given/When/Then format

**System Prompt:** The agent acts as an experienced product owner who turns vague feature ideas into sprint-ready user stories.

---

### 9. Ankit Pandey — README Generator Agent

**Use Case:** A developer pastes their project's main code file or a description of what their project does. The agent analyses the project and then writes a polished, complete README.

**Tool 1 — `analyze_project`**
- Input: the project's main code file or a plain description of the project
- Task: Identify what the project does, its key features, dependencies, how it's run, and who would use it
- Output: A structured project profile (purpose, features, tech stack, run instructions)

**Tool 2 — `write_readme`**
- Input: the project profile from Tool 1
- Task: Write a complete README with title, description, features list, installation steps, usage example, and tech stack — in clean Markdown
- Output: A ready-to-commit README.md

**System Prompt:** The agent acts as a developer-experience writer who makes any project instantly understandable from its README.

---

### 10. Piyush Tilara — Brand Name & Tagline Agent

**Use Case:** A user describes their new business or product idea. The agent generates strong brand name options and then crafts a tagline and elevator pitch for the best one.

**Tool 1 — `generate_name_options`**
- Input: a description of the business/product, its target customers, and the desired brand feel (e.g., premium, playful, techy)
- Task: Generate 6–8 brand name options with a one-line rationale for each, and mark the single strongest option
- Output: A list of name options with rationales and a recommended pick

**Tool 2 — `create_tagline_and_pitch`**
- Input: the recommended name from Tool 1 + the business description
- Task: Write 3 tagline options and a 30-second elevator pitch built around the chosen name
- Output: Three taglines plus a punchy elevator pitch paragraph

**System Prompt:** The agent acts as a branding consultant who gives new businesses a memorable name and a story to tell.

---

### 11. Mohit Luthra — Performance Review Writer Agent

**Use Case:** An employee pastes rough bullet points of what they did this year. The agent organises the accomplishments and then writes a polished self-review narrative.

**Tool 1 — `organize_accomplishments`**
- Input: rough bullet points of work done during the review period
- Task: Group the items into themes (delivery, collaboration, leadership, growth), quantify impact where possible, and flag which items are the strongest evidence
- Output: A structured accomplishment map grouped by theme with the strongest items highlighted

**Tool 2 — `write_review_narrative`**
- Input: the accomplishment map from Tool 1
- Task: Write a confident, professional self-review narrative — one short paragraph per theme — using specific, impact-first language (without exaggerating)
- Output: A complete self-review ready to paste into a performance review form

**System Prompt:** The agent acts as a career mentor who helps employees present their real work in its best, most honest light.

---

### 12. Rahul Dusane — Incident Postmortem Writer Agent

**Use Case:** An engineer pastes rough notes about a production incident. The agent reconstructs the timeline and impact, then writes a blameless postmortem document.

**Tool 1 — `build_incident_timeline`**
- Input: rough incident notes (alerts, chat snippets, what happened and when)
- Task: Reconstruct an ordered timeline of events, identify the trigger, the impact (who/what was affected and for how long), and how it was resolved
- Output: A structured timeline plus an impact summary

**Tool 2 — `write_postmortem_doc`**
- Input: the timeline and impact summary from Tool 1
- Task: Write a blameless postmortem with sections for Summary, Timeline, Root Cause, Impact, What Went Well, What Went Wrong, and Action Items — focusing on systems, never on blaming people
- Output: A complete postmortem document in Markdown

**System Prompt:** The agent acts as a site reliability engineer who turns messy incident notes into clear, blameless postmortems that make systems stronger.

---

### 13. Parth Kansara — Freelance Proposal Writer Agent

**Use Case:** A freelancer pastes a client's job brief and a note about their own skills. The agent defines the scope and pricing structure, then writes a winning proposal.

**Tool 1 — `define_scope_and_milestones`**
- Input: the client's job brief + the freelancer's relevant skills and experience
- Task: Break the job into clear deliverables and milestones, estimate effort per milestone, and suggest a pricing structure (fixed / hourly / per-milestone)
- Output: A scoped breakdown with deliverables, milestones, and a suggested pricing approach

**Tool 2 — `write_proposal`**
- Input: the scoped breakdown from Tool 1 + the freelancer's background
- Task: Write a persuasive proposal — a personalised opening that shows understanding of the client's problem, the proposed approach, deliverables and timeline, and a clear next step
- Output: A ready-to-send freelance proposal

**System Prompt:** The agent acts as a freelance business coach who writes proposals that win clients by showing understanding, not desperation.

---

### 14. Daryl Aw — Localization & Culture Adapter Agent

**Use Case:** A user provides text (marketing copy, app message, or announcement) plus a target language and country. The agent translates it and then adapts it culturally so it lands naturally with local readers.

**Tool 1 — `translate_text`**
- Input: the source text + target language and country (e.g., "Japanese for Japan", "Spanish for Mexico")
- Task: Produce an accurate, natural translation that preserves the original meaning and intent
- Output: The translated text with notes on any phrases that had no direct equivalent

**Tool 2 — `adapt_for_culture`**
- Input: the translation from Tool 1 + the target country
- Task: Adjust idioms, formality level, humour, examples, and references so the text feels written *for* that culture, not just translated into its language — flagging anything that could be confusing or offensive locally
- Output: The final localized text plus a short list of cultural adaptations made and why

**System Prompt:** The agent acts as a localization specialist who makes content feel native in every market, not just translated.

---

### 15. Akshaykumar More — Meeting Agenda Planner Agent

**Use Case:** A user describes an upcoming meeting — its goal, attendees, and duration. The agent designs a focused agenda and then time-boxes it with preparation prompts for attendees. (This is about planning a meeting *before* it happens — not summarizing notes afterwards.)

**Tool 1 — `design_agenda`**
- Input: meeting goal, attendee roles, and total duration
- Task: Define the discussion items needed to reach the goal, order them logically, and identify which attendee should lead each item — cutting anything that doesn't serve the goal
- Output: An ordered agenda with an owner and desired outcome per item

**Tool 2 — `timebox_and_prep`**
- Input: the agenda from Tool 1 + the meeting duration
- Task: Allocate minutes to each item (leaving buffer for decisions), and write a short pre-read note with 1–2 questions each attendee should think about beforehand
- Output: A time-boxed agenda plus a ready-to-send pre-meeting prep message

**System Prompt:** The agent acts as a chief of staff who designs meetings that start on time, stay on track, and end with decisions.

---

### 16. Bharat Chhabriya — 30-60-90 Day Plan Agent

**Use Case:** A user shares a job role they're about to start and a short description of the company. The agent analyses what success looks like in that role and then builds a concrete 30-60-90 day onboarding plan.

**Tool 1 — `analyze_role_expectations`**
- Input: the job title, key responsibilities, and a short company description
- Task: Identify what success looks like in this role — the skills to demonstrate, relationships to build, systems to learn, and early wins to target
- Output: A role-success profile covering learning priorities, key stakeholders, and candidate early wins

**Tool 2 — `build_30_60_90_plan`**
- Input: the role-success profile from Tool 1
- Task: Create a phased plan — Days 1–30 (learn), Days 31–60 (contribute), Days 61–90 (lead) — with specific goals, actions, and a measurable outcome for each phase
- Output: A complete 30-60-90 day plan, one section per phase

**System Prompt:** The agent acts as an executive onboarding coach who helps new hires make a strong, structured impact in their first 90 days.

---

## Evaluation Criteria

| Criteria | Points |
|---|---|
| Code follows the same LangChain agent structure as `email_humanizer_agent.py` | 20 |
| Both tools are implemented correctly using `@tool` and `PromptTemplate` | 20 |
| Agent runs end-to-end without errors | 20 |
| `README.md` clearly explains the use case and how to run it | 20 |
| GitHub repo is public, clean, and has `.env.example` (no real API key committed) | 20 |
| **Total** | **100** |

---

## Tips

- Start by running the original `email_humanizer_agent.py` first so you understand the flow
- Read the `README.md` in this repo — it explains the agent's think → act → observe loop
- Your `.env` file must never be pushed to GitHub — add it to `.gitignore`
- Test with simple inputs first before trying complex ones
- The `SYSTEM_PROMPT` is the brain of your agent — write it clearly, and tell the agent to always use Tool 1 first, then Tool 2

---

*Deadline and submission link: shared on WhatsApp. Post your GitHub URL in the Excel sheet.*
