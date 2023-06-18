class Course:
    course_counter = 1

    def __init__(self, course_name, course_level):
        self.course_id = Course.course_counter
        Course.course_counter += 1
        self.course_name = course_name
        self.course_level = course_level


class Student:
    student_counter = 1

    def __init__(self, student_name, student_level):
        self.student_id = Student.student_counter
        Student.student_counter += 1
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []

    def add_course(self, course):
        if course.course_level == self.student_level:
            self.student_courses.append(course)
            print("Course added successfully.")
        else:
            print("Cannot add course. Student level does not match course level.")

    def display_details(self):
        print("Student ID   :", {self.student_id})
        print("Student Name :", self.student_name)
        print("Student Level:", self.student_level)
        print("Courses Enrolled:")
        if self.student_courses:
            for course in self.student_courses:
                #print("Course ID:", course.course_id)
                print("Course Name:", course.course_name)
                #print("Course Level:", course.course_level)
        else:
            print("No courses enrolled.")


    def remove_course(self, course):
        if course in self.student_courses:
            self.student_courses.remove(course)
            print("Course Removed Successfully.")
        else:
            print("Course Not Found In Student's Enrolled Courses.")


def add_new_student():
    student_name = input("\nEnter Student Name: ")
    student_level = input("Select Student Level (A-B-C): ")
    while student_level not in ["A", "B", "C"]:
        print("Invalid level. Please select again.")
        student_level = input("Select Student Level (A-B-C): ")
    new_student = Student(student_name, student_level)
    students.append(new_student)
    print("Student saved successfully.")


def remove_student():
    student_id = int(input("\nEnter Student ID: "))
    found_student = None
    for student in students:
        if student.student_id == student_id:
            found_student = student
            break
    if found_student:
        students.remove(found_student)
        print("Student Deletion Successful.")
    else:
        print("Student Does Not Exist.")


def edit_student():
    student_id = int(input("\nEnter student ID: "))
    found_student = None
    for student in students:
        if student.student_id == student_id:
            found_student = student
            break
    if found_student:
        new_name = input("\nEnter New Name: ")
        new_level = input("Select New Level (A-B-C): ")
        while new_level not in ["A", "B", "C"]:
            print("Invalid Level. Please Select Again.")
            new_level = input("Select New Level (A-B-C): ")
        found_student.student_name = new_name
        found_student.student_level = new_level
        print("Student Details Updated Successfully.")
    else:
        print("Student Does Not Exist.")


def display_all_students():
    if students:
        for student in students:
            student.display_details()
            print("--------------------")
    else:
        print("No Students To Display.")


def create_new_course():
    course_name = input("\nEnter Course Name: ")
    course_level = input("Select Course Level (A-B-C): ")
    while course_level not in ["A", "B", "C"]:
        print("Invalid Level. Please Select Again.")
        course_level = input("Select Course Level (A-B-C): ")
    new_course = Course(course_name, course_level)
    courses.append(new_course)
    print("Course Created Successfully.")


def remove_course():
    course_id = int(input("\nEnter Course ID: "))
    found_course = None
    for course in courses:
        if course.course_id == course_id:
            found_course = course
            break
    if found_course:
        courses.remove(found_course)
        print("Course Deletion Successful.")
    else:
        print("Course Does Not Exist.")


def edit_course():
    course_id = int(input("\nEnter Course ID: "))
    found_course = None
    for course in courses:
        if course.course_id == course_id:
            found_course = course
            break
    if found_course:
        new_name = input("Enter New Course Name: ")
        new_level = input("Select New Course Level (A-B-C): ")
        while new_level not in ["A", "B", "C"]:
            print("Invalid Level. Please Select Again.")
            new_level = input("Select New Course Level (A-B-C): ")
        found_course.course_name = new_name
        found_course.course_level = new_level
        print("Course Details Updated Successfully.")
    else:
        print("Course Does Not Exist.")


def display_all_courses():
    if courses:
        for course in courses:
            print("Course ID:", {course.course_id})
            print("Course Name:", course.course_name)
            print("Course Level:", course.course_level)
            print("--------------------")
    else:
        print("No Courses To Display.")


def add_course_to_student():
    student_id = int(input("\nEnter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    found_student = None
    found_course = None
    for student in students:
        if student.student_id == student_id:
            found_student = student
            break
    for course in courses:
        if course.course_id == course_id:
            found_course = course
            break
    if found_student:
        if found_course:
            found_student.add_course(found_course)
        else:
            print("Course Does Not Exist.")
    else:
        print("Student Does Not Exist.")

def remove_course_from_student():
    student_id = int(input("\nEnter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    found_student = None
    found_course = None
    for student in students:
        if student.student_id == student_id:
            found_student = student
            break
    for course in courses:
        if course.course_id == course_id:
            found_course = course
            break
    if found_student:
        if found_course:
            found_student.remove_course(found_course)
        else:
            print("Course Does Not Exist.")
    else:
        print("Student Does Not Exist.")


students = []
courses = []

# Main program loop
while True:
    print("\n")
    print("|---------- Main Page -----------|")
    print("| 1 . Add New Student            |")
    print("| 2 . Remove Student             |")
    print("| 3 . Edit Student               |")
    print("| 4 . Display all Students       |")
    print("| 5 . Create New Course          |")
    print("| 6 . Remove Course              |")
    print("| 7 . Edit Course                |")
    print("| 8 . Display all Courses        |")
    print("| 9 . Add Course to Student      |")
    print("| 10. Remove Course from Student |")
    print("| q . Exit                       |")
    print("|ــــــــــــــــــــــــــــــــ|")
    choice = input("Enter Your Choice  1-10 or 'q'  To Exit: ")

    if choice == "1":
        add_new_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        edit_student()
    elif choice == "4":
        display_all_students()
    elif choice == "5":
        create_new_course()
    elif choice == "6":
        remove_course()
    elif choice == "7":
        edit_course()
    elif choice == "8":
        display_all_courses()
    elif choice == "9":
        add_course_to_student()
    elif choice == "10":
        remove_course_from_student()
    elif choice.lower() == "q":
        print("Exiting The Program. Goodbye!")
        break
    else:
        print("Invalid Choice. Please Select Again!!.")
