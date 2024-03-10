class Student:
    # default constructor
    def __init__(self,student_name,student_id):
        self.student_name = student_name # instance variable
        self.student_id = student_id     # instance variable
        #print(self.student_name, self.student_id)

    def display(self):
        print("Name: ", self.student_name, "Id: ",self.student_id)

s1 = Student("Bob",12)
s1.display()

