class Student:
    def __init__(self, name, student_id, gpa):
        self._name = name
        self._student_id = student_id
        self._gpa = gpa
        self._attendance = 0

    def mark_attendance(self):
        self._attendance += 1

    def get_attendance(self):
        return self._attendance

    def display_info(self):
        print(f"Student Name: {self._name}")
        print(f"Student ID: {self._student_id}")
        print(f"GPA: {self._gpa}")
        print(f"Attendance: {self._attendance}")



class Course:
    def __init__(self, course_name):
        self._course_name = course_name
        self._enrolled_students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self._enrolled_students.append(student)

    def remove_student(self, student):
        self._enrolled_students.remove(student)

    def list_students(self):
        for student in self._enrolled_students:
            student.display_info()
