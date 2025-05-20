class Course:
    def __init__(self, id, name, instructor):
        self.id = id
        self.name = name
        self.instructor = instructor
        self.students = {}
