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
