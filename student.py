students = []


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=None):
        """
        Student Constructor
        :param name: string - student name
        :param student_id: integer - optional student ID
        """
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return f"Student {self.name}"

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name