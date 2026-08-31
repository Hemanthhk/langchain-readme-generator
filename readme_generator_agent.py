"""README Generator Agent — a LangChain agent that analyzes a project
and writes a polished, production-ready README.

Setup: pip install -r requirements.txt, copy .env.example to .env, add your key.
Run:   python readme_generator_agent.py
"""

import logging
import os
import sys
from pathlib import Path

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
logger = logging.getLogger("readme_generator")

load_dotenv()
if not os.getenv("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY").startswith("sk-your"):
    logger.error("OPENAI_API_KEY not set. Copy .env.example to .env and add your key.")
    sys.exit(1)

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

# ----------------------------------------------------------------------
# Tools
# ----------------------------------------------------------------------

ANALYZE_PROMPT = PromptTemplate(
    input_variables=["project_input"],
    template="""You are a senior technical analyst and developer-experience writer.

Review the following project information and extract a clear project profile.
This may be either:
- a main code file
- a short description of the project
- a combination of both

Project information:
{project_input}

Your task is to identify:
- Project purpose and problem it solves
- Core features and capabilities
- Target users / audience
- Main technologies and dependencies
- How the project is run or launched
- Any setup requirements, environment variables, or important configuration
- Risks, limitations, or assumptions

Return a structured project profile in clear sections.
Keep it specific, factual, and practical.
Do not invent features that are not supported by the input.

Return ONLY the project profile, nothing else.""",
)

WRITE_README_PROMPT = PromptTemplate(
    input_variables=["project_profile"],
    template="""You are a developer-experience writer who turns technical projects into polished documentation.

Use the following project profile to write a complete README.md file in Markdown.

Project profile:
{project_profile}

Requirements:
- Include a strong project title and short summary
- Add a clear description of what the project does
- Include a features section with 4-8 bullet points
- Include a project structure section if relevant
- Include installation instructions
- Include usage examples or quick start steps
- Include technology stack / dependencies
- Include configuration notes for environment variables or setup if needed
- Include a section for who this is for / target audience
- Use clean, professional markdown formatting
- Make the README easy for developers to scan quickly
- If a detail is uncertain, write a realistic placeholder and clearly label it as a required customisation

Return ONLY the final README markdown, nothing else.""",
)


@tool
def analyze_project(project_input: str) -> str:
    """Analyze a project description or code file and extract a structured project profile. Use this FIRST."""
    logger.info("[analyze_project] analyzing project input")
    return llm.invoke(ANALYZE_PROMPT.format(project_input=project_input)).content


@tool
def write_readme(project_profile: str) -> str:
    """Write a polished README.md from a structured project profile. Use AFTER analyze_project."""
    logger.info("[write_readme] generating README")
    return llm.invoke(WRITE_README_PROMPT.format(project_profile=project_profile)).content


# ----------------------------------------------------------------------
# Agent
# ----------------------------------------------------------------------

SYSTEM_PROMPT = """You are a README Generator assistant. Your job is to help developers
turn a project description or code file into a polished instantly understandable README.md.

When the user gives you project information, follow these steps:
1. First, use the analyze_project tool to understand the project.
2. Then, use the write_readme tool to turn that analysis into a complete README.
3. Return the final README to the user.

Always use both tools in order: analyze first, then write the README."""

agent = create_agent(model=llm, tools=[analyze_project, write_readme], system_prompt=SYSTEM_PROMPT)


def resolve_project_input(project_input: str) -> tuple[str, Path | None]:
    """Return the project text and an optional source directory when a file or folder path is supplied."""
    cleaned_input = project_input.strip()
    candidate = Path(cleaned_input)

    if candidate.exists() and candidate.is_file():
        try:
            file_text = candidate.read_text(encoding="utf-8", errors="ignore")
            return file_text, candidate.parent
        except OSError:
            logger.warning("Could not read file %s, using raw input instead.", candidate)

    if candidate.exists() and candidate.is_dir():
        project_files = []
        for file_path in sorted(candidate.iterdir()):
            if file_path.is_file() and file_path.suffix.lower() in {".py", ".js", ".ts", ".java", ".go", ".rs", ".cs", ".cpp", ".c", ".md", ".txt"}:
                project_files.append(file_path)

        if project_files:
            content_parts = []
            for file_path in project_files[:5]:
                try:
                    content_parts.append(f"--- FILE: {file_path.name} ---\n{file_path.read_text(encoding='utf-8', errors='ignore')}\n")
                except OSError:
                    continue
            return "\n".join(content_parts), candidate

    return cleaned_input, None


def save_readme(readme: str, source_dir: Path | None = None) -> str:
    """Save the generated README.md to the project directory or current working directory."""
    target_dir = source_dir or Path.cwd()
    output_path = target_dir / "README.md"
    output_path.write_text(readme, encoding="utf-8")
    return str(output_path)


def run_readme_generator(project_input: str) -> str:
    """Run the agent on a project description or code file and return the final README."""
    result = agent.invoke({"messages": [HumanMessage(content=project_input)]})
    return result["messages"][-1].content


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def main() -> None:
    print("\nREADME GENERATOR AGENT (LangChain + OpenAI)")
    print("Paste a project description, a main code file path, a project folder path, or type 'quit' to exit.\n")

    while True:
        project_input = input("Project description / code path / folder path: ").strip()
        if not project_input:
            continue
        if project_input.lower() in ("quit", "exit", "q"):
            break

        try:
            project_text, source_dir = resolve_project_input(project_input)
            if project_text.strip().startswith("import ") or project_text.strip().startswith("def ") or project_text.strip().startswith("class ") or "\n" in project_text:
                project_text = project_text
            readme = run_readme_generator(project_text)
            output_path = save_readme(readme, source_dir)

            print("\n" + "=" * 80)
            print(readme)
            print("=" * 80 + "\n")
            print(f"README saved to: {output_path}\n")
        except Exception as e:
            logger.error("Agent failed: %s", e)


if __name__ == "__main__":
    main()
