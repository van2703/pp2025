students = []
courses = []
marks = {}
def number_of_students():
    n = int(input("Number of students: "))
    return n
def students(n):
    for i in range(n):
        print(f"\nstudent {i+1}")
        id = input("student ID: ")
        name = input("name: ")
        dob = input("date of Birth: ")

        student = {
            "id": id,
            "name": name,
            "doB": dob
        }
        students.append(student)

def number_of_courses():
    m = int(input("Number of courses: "))
    return m

def courses(m):
    for i in range(m):
        print(f"\ncourse {i+1}")
        id = input("course ID: ")
        name = input("course name: ")
        course = {
            "id": id,
            "name": name
        }
        courses.append(course)

def marks():
    for c in courses:
        print(f"{c['id']} - {c['name']}")
    course_id = input("Enter course ID: ")
    if course_id not in marks:
        marks[course_id] = {}
    print(f"\nInput marks for course {course_id}")
    for s in students:
        mark = float(input(f"Mark for {s['name']} (ID: {s['id']}): \n"))
        marks[course_id][s["id"]] = mark

def list_students():
    print("student list\n")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def list_courses():
    print("\ncourse list")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def student_marks():
    for c in courses:
        print(f"{c['id']} - {c['name']}")

    course_id = input("Enter course ID: ")

    if course_id not in marks:
        print("No marks for this course yet.")
        return

    print(f"\nmark for course {course_id}")
    for s in students:
        id = s["id"]
        if id in marks[course_id]:
            print(f"{s['name']} (ID: {id}) : {marks[course_id][id]}")
        else:
            print(f"{s['name']} (ID: {id}) : No mark")
def main():
    n = number_of_students()
    students(n)
    m = number_of_courses()
    courses(m)
    while True:
        print("1. list students")
        print("2. list courses")
        print("3. enter marks for a course")
        print("4. show student marks for a course")
        choice = input("Choose an option: ")

        if choice == "1":
            list_students()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            marks()
        elif choice == "4":
            student_marks()
        else:
            print("Invalid option. Try again.")