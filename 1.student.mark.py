students = []
courses = []

def input_students():
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        print("Student",i+1)
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = {'id': id, 'name': name, 'dob': dob, 'marks': {}}
        students.append(student)
    print("Students added successfully!\n")

def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        print("Course",i+1)
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = {'id': id, 'name': name, 'students': {}}
        courses.append(course)
    print("Courses added successfully!\n")

def input_marks():
    course_id = input("Enter course ID: ")
    course = next((c for c in courses if c['id'] == course_id), None)
    if not course:
        print("Invalid course ID")
        return

    for student in students:
        mark = input(f"Enter mark for student {student['name']}: ")
        course['students'][student['id']] = mark

    print("Marks added successfully!\n")

def list_courses():
    print("Courses:")
    for course in courses:
        print(f"- {course['name']} ({course['id']})")
    print()

def list_students():
    print("Students:")
    for student in students:
        print(f"- {student['name']} ({student['id']})")
    print()

def show_marks():
    course_id = input("Enter course ID: ")
    course = next((c for c in courses if c['id'] == course_id), None)
    if not course:
        print("Invalid course ID")
        return

    print(f"Marks for {course['name']} ({course['id']}):")
    for student_id, mark in course['students'].items():
        student = next((s for s in students if s['id'] == student_id), None)
        if not student:
            print(f"- {student_id}: {mark}")
        else:
            print(f"- {student['name']} ({student_id}): {mark}")
    print()

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
            input_students()
        elif sub_choice == '2':
            input_courses()
        elif sub_choice == '3':
            input_marks()
        else:
            print("Invalid choice")
    elif choice == '2':
        print("1. List courses")
        print("2. List students")
        print("3. Show student marks for a course")
        sub_choice = input("Enter your choice: ")
        if sub_choice == '1':
            list_courses()
        elif sub_choice == '2':
            list_students()
        elif sub_choice == '3':
            show_marks()
        else:
            print("Invalid choice")
    elif choice == '3':
        break
    else:
        print("Invalid choice")