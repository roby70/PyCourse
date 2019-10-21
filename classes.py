students = []


class Student:
    def __init__(self, name, student_id=None):
        student = {"name": name, "student_id": student_id}
        students.append(student)


student = Student("Mark")

print(students)
