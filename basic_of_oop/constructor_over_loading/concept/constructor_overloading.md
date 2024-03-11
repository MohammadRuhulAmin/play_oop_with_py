### What is constructor overloading?
>In Python, constructor overloading is not directly supported like in languages such as Java or C++. However, you can achieve similar functionality by using default parameter values. 


```python

class student:
    def __init__(self,*info):
        if len(info) == 3:
            self.name = info[0]
            self.id = info[1]
            self.cgpa = info[2]
        elif len(info) == 2:
            self.name = info[0]
            self.id = info[1]
        else: self.name = info[1]
        print("Student object created!")

s1 = student("Carol",12,3.5)
s3 = student("Badol",19,4.0)
```