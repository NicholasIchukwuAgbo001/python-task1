class CourseManagementSystem:
    def __init__(self):
        self.users = []
        self.courses = []
        self.logged_in = None

    def create_course(self, course):
        if self.logged_in.role != "instructor":
            raise Exception("Not authorized")
        self.courses.append(course)
        self.logged_in.courses.append(course)

    def enroll_student(self, student, course):
        if student.role != "student" or course not in self.courses:
            raise Exception("Not authorized or course not found")
        course.students[student.email] = {"grade": None}
        student.courses.append(course)

    def score_student(self, student_email, course, grade):
        if self.logged_in.role != "instructor" or course not in self.logged_in.courses:
            raise Exception("Not authorized")
        if student_email not in course.students:
            raise Exception("Student not found")
        course.students[student_email]["grade"] = grade

    def view_courses(self):
        if self.logged_in:
            if self.logged_in.role == "student":
                courses_info = []
                for course in self.logged_in.courses:
                    courses_info.append({"name": course.name, "instructor": course.instructor.email})
                return courses_info
            elif self.logged_in.role == "instructor":
                courses_info = []
                for course in self.logged_in.courses:
                    students_info = []
                    for student_email, student_info in course.students.items():
                        students_info.append({"email": student_email, "grade": student_info["grade"]})
                    courses_info.append({"name": course.name, "students": students_info})
                return courses_info
        else:
            raise Exception("You must be logged in to view courses.")

    def view_grade(self, course):
        if not self.logged_in or self.logged_in.email not in course.students:
            raise Exception("Not authorized or not enrolled")
        return course.students[self.logged_in.email]["grade"]

    def register_user(self, user):
        for existing_user in self.users:
            if existing_user.email == user.email:
                raise Exception("Email already exists")
        self.users.append(user)

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                self.logged_in = user
                return
        raise Exception("Invalid credentials")
