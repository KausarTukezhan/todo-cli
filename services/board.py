from config import session
from models.board import Board


class BoardService:
    def select_board(self, user):
        boards = session.query(Board).filter_by(user_id=user.id).all()
        if not boards:
            print("You don't have any boards. Create a new one.")
            return self.create_board(user)
        print("Select a board:")
        for board in boards:
            print(f"{board.id}. {board.name}")
        board_id = int(input("Enter the board ID: "))
        return session.query(Board).filter_by(id=board_id, user_id=user.id).first()

    def create_board(self, user):
        board_name = input("Enter the name of the new board: ")
        board = Board(name=board_name, user=user)
        session.add(board)
        session.commit()
        print("Board created!")
        return board

boardService = BoardService()