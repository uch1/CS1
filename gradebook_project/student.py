class Student():
    '''
    student id, student name, student grade, gpa, assignments
    '''
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.assignment = {}

    def add_assignment(self, assignment, grade):
        self.assignment[assignment] =  grade

    def get_assignments(self):
        return self.assignment

    def delete_assignment(self, assignment):
        self.assignment.pop(assignment)

    def update_assignment(self, old_assignment, new_assignment, grade):
        self.delete_assignment(old_assignment)
        self.add_assignment(new_assignment, grade)

    def get_gpa(self):
        list_of_assignments = self.get_assignments()

        total = 0
        for grade in list_of_assignments.values():
            total += grade
        num_of_assignments = len(list_of_assignments)
        gpa = total / num_of_assignments
        return gpa
        #return total / len(list_of_assignments)
