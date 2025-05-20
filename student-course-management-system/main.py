from student import Student
from instructor import Instructor
from course import Course
from courseManagementSystem import CourseManagementSystem

def main():
    course_management_system = CourseManagementSystem()
    user_id = 1
    course_id = 1
    user = ""
    while True:
        if not course_management_system.logged_in:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                email = input("Enter email: ")
                password = input("Enter password: ")
                role = input("Enter role (student/instructor): ")
                if role == "student":
                    user = Student(user_id, email, password)
                    print("Student registered successfully")
                elif role == "instructor":
                    user = Instructor(user_id, email, password)
                    print("Instructor registered successfully")
                course_management_system.register_user(user)
                user_id += 1
            elif choice == "2":
                email = input("Enter email: ")
                password = input("Enter password: ")
                course_management_system.login(email, password)
            elif choice == "3":
                print("Existing the app, bye")
                break
        else:
            print("1. Create Course")
            print("2. Enroll in Course")
            print("3. Score Student")
            print("4. View Courses")
            print("5. View Grade")
            print("6. Logout")
            choice = input("Enter your choice: ")
            if choice == "1":
                if course_management_system.logged_in.role == "instructor":
                    name = input("Enter course name: ")
                    course = Course(course_id, name, course_management_system.logged_in)
                    course_management_system.create_course(course)
                    course_id += 1
                else:
                    print("You are not authorized to create courses.")
            elif choice == "2":
                if course_management_system.logged_in.role == "student":
                    course_name = input("Enter course name: ")
                    for course in course_management_system.courses:
                        if course.name == course_name:
                            course_management_system.enroll_student(course_management_system.logged_in, course)
                            break
                    else:
                        print("Course not found.")
                else:
                    print("You are not authorized to enroll in courses.")
            elif choice == "3":
                if course_management_system.logged_in.role == "instructor":
                    course_name = input("Enter course name: ")
                    student_email = input("Enter student email: ")
                    grade = input("Enter grade: ")
                    for course in course_management_system.logged_in.courses:
                        if course.name == course_name:
                            course_management_system.score_student(student_email, course, grade)
                            break
                    else:
                        print("Course not found.")
                else:
                    print("You are not authorized to score students.")
            elif choice == "4":
                course_management_system.view_courses()
            elif choice == "5":
                course_name = input("Enter course name: ")
                for course in course_management_system.logged_in.courses:
                    if course.name == course_name:
                        course_management_system.view_grade(course)
                        break
                else:
                    print("Course not found.")
            elif choice == "6":
                course_management_system.logged_in = None

if __name__ == "__main__":
    main()