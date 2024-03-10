class Student:
    # default constructor
    def __init__(self,student_name,student_id,contact):
        self.student_name = student_name # instance variable
        self.student_id = student_id     # instance variable
        self.contact = contact
        #print(self.student_name, self.student_id)

    def display(self):
        print("Name: ", self.student_name, "Id: ",self.student_id)

s1 = Student("Bob",12,"01322352864")
s1.display()
print(dir(s1))
print(s1.__dict__)

