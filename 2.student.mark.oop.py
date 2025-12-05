class student:
    def __init__(self, student_id, student_name, doB):
        self.id = student_id
        self.name =student_name
        self.dob = doB
class course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name
class school:
    def __init__(self):
        self.student = []
        self.course = []
        self.mark = {}
    def add_student(self):
        student_id = input("Student ID: ")
        student_name = input("Name: ")
        dob = input("Date of birth: ")
        s = student(student_id, student_name, dob)
        self.student.append(s)
    def add_course(self):
        course_id = input("Course ID: ")
        course_name = input("course name: ")
        c = course(course_id, course_name)
        self.course.append(c)
    def add_mark(self):
        for c in self.course:
            print(f"{c.id}, {c.name}: ")
        course_id = input("Enter course ID: ")
        if course_id not in self.mark:
            self.mark[course_id] = {}
        print(f"\nInput marks for course {course_id}")
        for s in self.student:
            mark = float(input(f"Mark for {s.name} (ID: {s.id}): "))
            self.mark[course_id][s.id] = mark
    def list_student(self):
        print("\n Student list: ")
        for s in self.student:
            print(f"ID: {s.id}, name: {s.name}, doB: {s.dob}")
    def list_course(self):
        print("\n course list: ")
        for c in self.course:
            print(f"ID: {c.id}, name: {c.name}")
    def show_mark(self):
        for c in self.course:
            print(f"{c.id}, {c.name}: ")
        course_id = input("Enter course ID: ")
        if course_id not in self.mark:
            print("No marks for this course yet.")
            return
        print(f"\nMarks for course {course_id}:")
        for s in self.student:
            student_id = s.id
            if student_id in self.mark[course_id]:
                print(f"{s.name} (ID: {student_id}): {self.mark[course_id][student_id]}")
            else:
                print(f"{s.name} (ID: {student_id}): No mark")
def main():
    sch = school()
    n_s = int(input("Number of students: "))
    for _ in range(n_s):
        sch.add_student()
    n_c = int(input("Number of courses: "))
    for _ in range(n_c):
        sch.add_course()
    while True:
        print("\n1. List students")
        print("2. List courses")
        print("3. Enter marks")
        print("4. Show marks")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            sch.list_student()
        elif choice == "2":
            sch.list_course()
        elif choice == "3":
            sch.add_mark()
        elif choice == "4":
            sch.show_mark()
        else:
            break
main()
