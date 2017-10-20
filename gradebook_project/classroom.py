class Classroom():
    #TODO: CRUD get assignments, delete student, add assignment to one and more students, delete assignment
    def __init__(self, class_name):
        self.class_name = class_name
        self.roster = {}

    def add_student(self, student):
        self.roster[student.student_id] = student

    def get_students(self):
        return self.roster

    def delete_student(self, student):
        self.roster.pop(student)

    def get_assignments(self, student):
        return student.get_assignments()

    def add_assignments(self, student, assignment, grade):
        student.add_assignment(assignment, grade)

    def delete_assignment(self, student, assignment):
        student.delete_assignment(assignment)
