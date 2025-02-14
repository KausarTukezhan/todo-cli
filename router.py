from services.auth import authService
from services.board import boardService
from services.task import taskService


def router():
    print("1. Register\n2. Login")
    choice = input("Choose an action: ")
    user = None
    while not user:
        if choice == "1":
            user = authService.register()
        elif choice == "2":
            user = authService.login()

    if user:
        board = boardService.select_board(user)
        while True:
            print(
                "1. Add task\n2. List tasks\n3. Edit task\n4. Change task status\n5. Delete task\n6. Create new board\n7. Select another board\n8. Exit"
            )
            action = input("Choose an action: ")
            if action == "1":
                taskService.add_task(user, board)
            elif action == "2":
                taskService.list_tasks(user, board)
            elif action == "3":
                taskService.update_task()
            elif action == "4":
                taskService.change_task_status()
            elif action == "5":
                taskService.delete_task()
            elif action == "6":
                board = boardService.create_board(user)
            elif action == "7":
                board = boardService.select_board(user)
            elif action == "8":
                break
