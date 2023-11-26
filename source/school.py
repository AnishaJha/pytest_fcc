class TooManyStudents(Exception):
    pass


class ClassRoom:
    def __init__(self, teacher, students, course_name):
        self.teacher = teacher
        self.students = students
        self.course_name = course_name

    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            raise TooManyStudents

    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                break

    def change_teacher(self, teacher):
        self.teacher = teacher


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    pass


class Student(Person):
    pass


