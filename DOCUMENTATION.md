# To-Do List CLI Application

A command-line to-do list application with authentication, task categorization, prioritization, filtering, and board management. Built with Python and SQLAlchemy.

## Features
- User authentication (registration & login)
- Task management (add, edit, delete, mark as complete/incomplete)
- Task categorization
- Task prioritization (low, medium, high)
- Task filtering (by category, priority, and status)
- Task searching by name
- Board-based task management
- Data persistence using SQLite

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KausarTukezhan/todo-cli.git
   cd todo-cli
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python main.py
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```
2. Choose an option:
   - Register/Login
   - Select or create a board
   - Manage tasks (add, edit, filter, complete, delete)
   
## Dependencies
- Python 3+
- SQLAlchemy

