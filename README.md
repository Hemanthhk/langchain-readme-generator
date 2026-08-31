# README Generator - LangChain Single Agent Project

A beginner-friendly project that teaches you how to build a **single agent** using **LangChain + OpenAI**. This agent can take any of the following:

- a short project description
- a main code file path
- a project folder path

and generates a polished, ready-to-use `README.md` for that project, saving it in the correct project directory.

## What You'll Learn

- How to design a two-step agent workflow
- How to use `PromptTemplate` to shape LLM output
- How to build reusable tools with the `@tool` decorator
- How `create_agent` connects tools and instructions together
- How to convert raw project info into clean documentation

## How It Works

```
User provides project description, code file, or project folder
       |
       v
  [Input detection] --> identifies whether the input is text, a file, or a folder
       |
       v
  [Agent thinks: "I need to understand the project first"]
       |
       v
  [Tool: analyze_project] --> extracts purpose, features, stack, setup, and users
       |
       v
  [Agent thinks: "Now I should draft the README"]
       |
       v
  [Tool: write_readme] --> creates a full Markdown README
       |
       v
  [Auto-save] --> writes README.md in the relevant project directory
       |
       v
  Final README returned to the user
```

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Langchain_sample_project.git
cd Langchain_sample_project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy the example env file and add your real key:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder:

```env
OPENAI_API_KEY=sk-your-actual-key-here
```

## Run

```bash
python readme_generator_agent.py
```

You will see a prompt like this:

```text
README GENERATOR AGENT (LangChain + OpenAI)
Paste a project description, a main code file path, a project folder path, or type 'quit' to exit.

Project description / code path / folder path:
```

The agent accepts:

- direct project descriptions
- a file path such as `C:\project\main.py`
- a folder path such as `C:\project_folder`

It then generates the README and saves it as `README.md` in the same directory as the project source or folder.

## Sample Input to Paste

You can paste the contents of the file [README_GENERATOR_sample_input.txt](README_GENERATOR_sample_input.txt), or use a project file/folder path directly. The examples below show both options.

### Option 1: Paste a project description

You can copy the text below directly into the prompt.

```text
Project Name: TaskFlow Manager

TaskFlow Manager is a lightweight Python CLI application for managing personal tasks and daily priorities. Users can add tasks, mark them as complete, view pending tasks, and filter them by category or deadline. The project is meant for individuals who want a simple local productivity tool without needing a heavy database or web app.

Core features:
- Add new tasks with title, description, category, and due date
- Mark tasks as complete
- View all tasks or only incomplete tasks
- Sort tasks by priority or deadline
- Save tasks to a JSON file for persistence
- Search tasks by keyword

Tech stack:
- Python 3.10+
- Standard library only (json, datetime, pathlib)
- Optional CLI library: argparse

How it works:
- The app loads tasks from a local JSON file when it starts
- Users interact with the command line to create, complete, or list tasks
- Changes are saved back to the file automatically

Target users:
- Students
- Freelancers
- Busy professionals who want a simple task organizer

Install and run:
- Create a virtual environment
- Install requirements
- Run python app.py
```

### Option 2: Use a file or folder path

```text
C:\Users\YourName\Desktop\TaskFlowManager
```

or

```text
C:\Users\YourName\Desktop\TaskFlowManager\app.py
```

The agent reads that project and saves a generated `README.md` in that same directory.

### Example: project folder flow

Suppose you have a project folder like this:

```text
C:\Users\YourName\Desktop\TaskFlowManager
├── app.py
├── utils.py
├── requirements.txt
└── README.md   # generated later by the agent
```

When you enter:

```text
C:\Users\YourName\Desktop\TaskFlowManager
```

The agent detects the folder, analyzes the files inside it, writes a detailed README, and saves it as:

```text
C:\Users\YourName\Desktop\TaskFlowManager\README.md
```

## Example Output Preview

The agent will generate README sections like:

- Project Title
- Overview
- Features
- Installation
- Usage
- Configuration
- Tech Stack
- Project Structure
- Target Audience
- License

## Project Structure

```
.
├── readme_generator_agent.py   # Main README generator agent
├── README_GENERATOR.md         # Project documentation for this agent
├── README_GENERATOR_sample_input.txt  # Sample input for testing the agent
├── requirements.txt            # Python dependencies
├── .env.example                # API key template
├── .gitignore                  # Keeps secrets and venv out of git
├── README.md                   # Readme generator project output
```

## Tech Stack

- [LangChain](https://python.langchain.com/) - Framework for building LLM applications
- [OpenAI GPT-4.1-mini](https://platform.openai.com/) - The LLM powering the agent
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management
- [Python](https://www.python.org/) - Main language used to build the app

## Notes

This project is useful for developers who want to turn rough project ideas, source files, or entire folders into professional documentation without writing a README from scratch.

The latest version also handles auto-save and project-path detection so the generated README lands exactly where the project lives.
