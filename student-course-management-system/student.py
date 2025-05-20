from user import User

class Student(User):
    def __init__(self, id, email, password):
        super().__init__(id, email, password, "student")
        self.courses = []
