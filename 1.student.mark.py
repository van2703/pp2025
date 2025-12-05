students = []
courses = []
marks = {}

def number_of_students():
    n = int(input("Number of students: "))
    return n

def input_students(n):
    for i in range(n):
        print(f"\nStudent {i+1}")
        sid = input("Student ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")

        student = {
            "id": sid,
            "name": name,
            "dob": dob
        }
        students.append(student)

def number_of_courses():
    m = int(input("Number of courses: "))
    return m

def input_courses(m):
    for i in range(m):
        print(f"\nCourse {i+1}")
        cid = input("Course ID: ")
        name = input("Course name: ")

        course = {
            "id": cid,
            "name": name
        }
        courses.append(course)

def input_marks():
    # show available courses
    for c in courses:
        print(f"{c['id']} - {c['name']}")

    course_id = input("Enter course ID: ")

    # create empty mark list if not exist
    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nInput marks for course {course_id}")
    for s in students:
        mark = float(input(f"Mark for {s['name']} (ID: {s['id']}): "))
        marks[course_id][s["id"]] = mark

def list_students():
    print("\nStudent list:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def list_courses():
    print("\nCourse list:")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def show_student_marks():
    for c in courses:
        print(f"{c['id']} - {c['name']}")

    course_id = input("Enter course ID: ")

    if course_id not in marks:
        print("No marks for this course yet.")
        return

    print(f"\nMarks for course {course_id}")
    for s in students:
        sid = s["id"]
        if sid in marks[course_id]:
            print(f"{s['name']} (ID: {sid}) : {marks[course_id][sid]}")
        else:
            print(f"{s['name']} (ID: {sid}) : No mark")

def main():
    n = number_of_students()
    input_students(n)

    m = number_of_courses()
    input_courses(m)

    while True:
        print("\n=== Menu ===")
        print("1. List students")
        print("2. List courses")
        print("3. Enter marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_students()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            show_student_marks()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

main()