import book as bk
from basic_of_oop.basic_class.code.ref_class import Student as Std
b1 = bk.Book("Opekkha","Humayun Ahmed")
b1.details()
b1.set_price(255)
b1.details()

s1 = Std.Student("Bob",12,"01322352864")
s1.display()
