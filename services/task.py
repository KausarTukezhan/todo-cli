from config import session
from models.category import Category
from models.task import Task


class TaskService:
    def add_task(self, user, board):
        description = input("Enter task description: ")
        category_name = input("Enter category: ")
        priority = input("Priority (low, medium, high): ")
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            session.add(category)
            session.commit()
        task = Task(
            description=description,
            priority=priority,
            category=category,
            board=board,
            user=user,
        )
        session.add(task)
        session.commit()
        print("Task added!")

    def update_task(self):
        task_id = int(input("Enter task ID to edit: "))
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            task.description = input("Enter new description: ")
            task.priority = input("Enter new priority (low, medium, high): ")
            session.commit()
            print("Task updated!")
        else:
            print("Task not found.")

    def delete_task(self):
        task_id = int(input("Enter task ID to edit: "))
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
            print("Task deleted!")
        else:
            print("Task not found.")

    def change_task_status(self):
        task_id = int(input("Enter task ID to change status: "))
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            task.completed = not task.completed
            session.commit()
            print("Task status changed!")
        else:
            print("Task not found.")

    def list_tasks(self, user, board):
        filter_category = input("Enter category to filter (or press Enter for all): ")
        filter_priority = input("Enter priority to filter (or press Enter for all): ")
        filter_status = input(
            "Enter status (completed/not completed or press Enter for all): "
        )
        search_query = input("Enter text to search in tasks (or press Enter for all): ")

        query = session.query(Task).filter_by(user_id=user.id, board_id=board.id)
        if filter_category:
            query = query.join(Category).filter(Category.name == filter_category)
        if filter_priority:
            query = query.filter(Task.priority == filter_priority)
        if filter_status.lower() == "completed":
            query = query.filter(Task.completed == True)
        elif filter_status.lower() == "not completed":
            query = query.filter(Task.completed == False)
        if search_query:
            query = query.filter(Task.description.ilike(f"%{search_query}%"))

        tasks = query.all()
        if not tasks:
            print("No tasks found.")
            return
        for task in tasks:
            status = "✔" if task.completed else "✘"
            print(
                f"[{task.id}] [{status}] {task.description} - {task.priority} ({task.category.name})"
            )


taskService = TaskService()
