"""Email Humanizer Agent — a LangChain agent that drafts an email from an idea,
then rewrites it to sound natural and human.

Setup: pip install -r requirements.txt, copy .env.example to .env, add your key.
Run:   python email_humanizer_agent.py
"""

import logging
import os
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("email_humanizer")

load_dotenv()
if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("sk-your"):
    logger.error("OPENAI_API_KEY not set. Copy .env.example to .env and add your key.")
    sys.exit(1)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

# ----------------------------------------------------------------------
# Tools
# ----------------------------------------------------------------------

DRAFT_PROMPT = PromptTemplate(
    input_variables=["idea"],
    template="""You are a professional email writer.
Given the following idea, write a structured email draft.

Idea: {idea}

Write the email with:
- A clear subject line
- Professional greeting
- Well-organized body (2-3 short paragraphs)
- Professional closing

Return ONLY the email, nothing else.""",
)

HUMANIZE_PROMPT = PromptTemplate(
    input_variables=["draft"],
    template="""You are an expert at making emails sound human and natural.

Take this email draft and rewrite it to sound like a real person wrote it.

Rules:
- Use contractions (I'm, we're, don't, can't)
- Vary sentence length (mix short and long sentences)
- Add a touch of warmth and personality
- Remove corporate jargon and stiff phrases
- Keep it professional but approachable
- Keep the same core message and structure
- Make it sound like something you'd actually send to a colleague

Email draft:
{draft}

Return ONLY the humanized email, nothing else.""",
)


@tool
def draft_email(idea: str) -> str:
    """Create a structured email draft from a brief idea. Use this FIRST."""
    logger.info("[draft_email] drafting: %s", idea)
    return llm.invoke(DRAFT_PROMPT.format(idea=idea)).content


@tool
def humanize_email(draft: str) -> str:
    """Rewrite a formal email draft to sound warm and natural. Use AFTER draft_email."""
    logger.info("[humanize_email] humanizing draft")
    return llm.invoke(HUMANIZE_PROMPT.format(draft=draft)).content


# ----------------------------------------------------------------------
# Agent
# ----------------------------------------------------------------------

SYSTEM_PROMPT = """You are an Email Humanizer assistant. Your job is to help users
write natural, human-sounding emails.

When the user gives you an email idea, follow these steps:
1. First, use the draft_email tool to create a structured email draft.
2. Then, use the humanize_email tool to make the draft sound natural and warm.
3. Return the final humanized email to the user.

Always use both tools in order: draft first, then humanize."""

agent = create_agent(model=llm, tools=[draft_email, humanize_email], system_prompt=SYSTEM_PROMPT)


def run_email_humanizer(email_idea: str) -> str:
    """Run the agent on an email idea and return the humanized email."""
    result = agent.invoke({"messages": [HumanMessage(content=email_idea)]})
    return result["messages"][-1].content


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def main() -> None:
    print("\nEMAIL HUMANIZER AGENT (LangChain + OpenAI)")
    print("Describe the email you want to write. Type 'quit' to exit.\n")

    while True:
        email_idea = input("Your email idea: ").strip()
        if not email_idea:
            continue
        if email_idea.lower() in ("quit", "exit", "q"):
            break

        try:
            email = run_email_humanizer(email_idea)
            print("\n" + "=" * 60)
            print(email)
            print("=" * 60 + "\n")
        except Exception as e:
            logger.error("Agent failed: %s", e)


if __name__ == "__main__":
    main()
