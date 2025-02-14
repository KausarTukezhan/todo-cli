import hashlib
from config import session
from models.user import User


class AuthService:
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = self.hash_password(password)
        user = User(username=username, password=hashed_password)
        session.add(user)
        session.commit()
        print("Registration successful!")
        return user

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        hashed_password = self.hash_password(password)
        user = (
            session.query(User)
            .filter_by(username=username, password=hashed_password)
            .first()
        )
        if user:
            print("Login successful!")
            return user
        else:
            print("Invalid credentials!")
            return None

authService = AuthService()