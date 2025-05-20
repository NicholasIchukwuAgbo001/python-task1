from user import User

class Instructor(User):
    def __init__(self, id, email, password):
        super().__init__(id, email, password, "instructor")
        self.courses = []
