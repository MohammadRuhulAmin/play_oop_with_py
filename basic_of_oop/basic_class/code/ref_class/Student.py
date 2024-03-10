class Student:
    # default constructor
    def __init__(self,student_name,student_id,contact):
        self.student_name = student_name # instance variable
        self.student_id = student_id     # instance variable
        self.contact = contact
        #print(self.student_name, self.student_id)

    def display(self):
        print("Name: ", self.student_name, "Id: ",self.student_id)
    
    def compare_object(self,temp_obj):
        if self.student_name == temp_obj.student_name:print("same object")
        else:print("not same object")

s1 = Student("Bob",12,"01322352864")
s1.display()
print(dir(s1))
print(s1.__dict__)

s2 = Student("ruhul",122,"121")
s1.compare_object(s2)

