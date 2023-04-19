class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = {}

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for i in range(num_students):
            print("Student",i+1)
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.students.append(student)
        print("Students added successfully!\n")

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for i in range(num_courses):
            print("Course",i+1)
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(id, name)
            self.courses.append(course)
        print("Courses added successfully!\n")

    def input_marks(self):
        course_id = input("Enter course ID: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            print("Invalid course ID")
            return

        for student in self.students:
            mark = input(f"Enter mark for student {student.name}: ")
            course.students[student.id] = mark

        print("Marks added successfully!\n")

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"- {course.name} ({course.id})")
        print()

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"- {student.name} ({student.id})")
        print()

    def show_marks(self):
        course_id = input("Enter course ID: ")
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            print("Invalid course ID")
            return

        print(f"Marks for {course.name} ({course.id}):")
        for student_id, mark in course.students.items():
            student = next((s for s in self.students if s.id == student_id), None)
            if not student:
                print(f"- {student_id}: {mark}")
            else:
                print(f"- {student.name} ({student_id}): {mark}")
        print()

    def run(self):
        while True:
            print("1. Input functions")
            print("2. Listing functions")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                print("1. Input students")
                print("2. Input courses")
                print("3. Input marks")
                sub_choice = input("Enter your choice: ")
                if sub_choice == '1':
                    self.input_students()
                elif sub_choice == '2':
                    self.input_courses()
                elif sub_choice == '3':
                    self.input_marks()
                else:
                    print("Invalid choice")
            elif choice == '2':
                print("1. List courses")
                print("2. List students")
                print("3. Show student marks for a course")
                sub_choice = input("Enter your choice: ")
                if sub_choice == '1':
                    self.list_courses()
                elif sub_choice == '2':
                    self.list_students()
                elif sub_choice == '3':
                    self.show_marks()
                else:
                    print("Invalid choice")
            elif choice == '3':
                break
            else:
                print("Invalid choice")

if __name__ == '__main__':
    school = School()
    school.run()