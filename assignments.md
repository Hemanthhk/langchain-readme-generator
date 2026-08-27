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

### 1. nisargkadam23@gmail.com — Article Simplifier Agent

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

### 2. vasentsethia@gmail.com — Commit Message & Changelog Agent

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

### 3. Korde.sachin@gmail.com — Blog Post Writer Agent

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

### 4. Lokeshmargana9@Gmail.com — Plant Care Advisor Agent

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

### 5. tadikondavishnu1@gmail.com — FAQ Generator Agent

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

### 6. rohanjs94blr@gmail.com — Debate Coach Agent

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

### 7. thumati.ragavendrachary@gmail.com — Trip Packing Assistant Agent

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

### 8. kedarpuja.239@gmail.com — User Story Generator Agent

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

### 9. hemanthhppl@gmail.com — README Generator Agent

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

### 10. vishalghume.ai@gmail.com — Brand Name & Tagline Agent

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

### 11. firdos.cs028@gmail.com — Performance Review Writer Agent

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
