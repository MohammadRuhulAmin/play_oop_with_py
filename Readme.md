<h1 align = "center">Play With Python</h1>

### what is class in object oriented programming ?
> A class is athe blue print for the objects, created from the class.
> Each class contains some data definitions (called fields), togeter with methods to manipulate that data.
> When the object is instantiated from the class, an instance variable is created for each field in the class.

### What is object of a class ?
> object are the basic run time entities in an object oriented system, an instance of a class, objects are the variables of the type class.

### Show a relation between Object and Class.
<img src="./public/images/class/class_object_relation.png" alt="Alternative text" width="300" height="200">

### Discribe the components of a class.
<img src="./public/images/class/class_components.png" alt="Alternative text" width="300" height="200">

### What is Method?
> A python method is like a python function. it must be called on an object which need to be put inside a class, can return statement.

### Show an Example of class and object.
<img src="./public/images/class/class_object_example.png" alt="Alternative text" width="300" height="200">

### What is Constructor?
- A special kind of method we use to initialize instance members of that class.
- It is used for initializing the instance members when we create the object of a class.
- If you create4 four objects, the class constructor will call four times.
- Every class must have a constructor, even if it simply relies on the default constructor.
- constructors can be two types.
  - Non-parameterized constructor (Default Constructor)
  - Parameterized Constructor


```python
#Example of a default constructor
class Employee:
    def __init__(self):
        print("Employee object Created")

emp1 = Employee()
emp2 = Employee()
``` 
### Output: 
> Employee object Created <br>
> Employee object Created

```python
class Employee:
    def__init__(self,name):
        # instance variable
        self.name = name
        print(self.name, "created!")

#instance 1
emp1 = Employee("John")
#instance 2
emp2 = Employee("David")
```
### Output: 
> John created <br>
> David created

### What is Constructor?
- A special kind of method we use to initialize instance members of that class.
- It is used for initializing the instance members when we create the object of a class.
- If you create4 four objects, the class constructor will call four times.
- Every class must have a constructor, even if it simply relies on the default constructor.
- constructors can be two types.
  - Non-parameterized constructor (Default Constructor)
  - Parameterized Constructor


```python
#Example of a default constructor
class Employee:
    def __init__(self):
        print("Employee object Created")

emp1 = Employee()
emp2 = Employee()
``` 
### Output: 
> Employee object Created <br>
> Employee object Created

```python
class Employee:
    def__init__(self,name):
        # instance variable
        self.name = name
        print(self.name, "created!")

#instance 1
emp1 = Employee("John")
#instance 2
emp2 = Employee("David")
```
### Output: 
> John created <br>
> David created

### What is Instance Method ? 
- Instance Method are methods which require an object of its class to be created before it can be called.
- Instance methods need a class instance and can access the instance through __self__.
- Instance method takes more than one paramenter,__self__, which points to an instance of a class.
- The __self__ parameter, instance methods can freely access attributes and other methods on the same object.

```python
class Employee: #class / design / blue print
    #parametrized constructor
    def __init__(self,name,no):
        self.no = no #instance variable
        self.name = name # instance variable
        contact = "+880-xxxxxxx" # Local variable

    # instance method
    def display(self):
        print(self.name,self.no)
   
emp1 = Employee("John",11) #instance 1
emp2 = Employee("David",12) #instance 2 object / Instance
emp1.display()
emp2.display()
```
### What is the use of __dict__ and dir()? 
> if argument is given, it returns a list of valid attributes for that object.

```python
s1 = Student("Bob",12,"01322352864")
s1.display()
print(dir(s1))
```

### output of dir() method:
```python 
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'contact', 'display', 'student_id', 'student_name']
```

> The __dict__ in Python represents a dictionary or any mapping object that is used to store the attributes of the object.
```python
s1 = Student("Bob",12,"01322352864")
s1.display()
print(s1.__dict__)
```

### output of __dict__ method:

```python
{'student_name': 'Bob', 'student_id': 12, 'contact': '01322352864'}
```

### How to use from and import ? 
> when classes are in same directory,to access a specific class, we will use import,<br>
otherwise we will use from <dic_path> import <class_name>

```python
import book as bk
b1 = bk.Book("Opekkha","Humayun Ahmed")
b1.details()
b1.set_price(255)
b1.details()
```

### What is pass by value and pass by reference in oop? 
>In Python, objects are passed by reference, so modifications to mutable objects within functions affect the original object; however, immutable objects behave like pass by value, preserving the original value outside the function.

```python
class Example:
    def __init__(self, value):
        self.value = value

def modify_value(obj):
    obj.value = "modified"  # This will modify the original object

def modify_immutable(value):
    value = "modified"  # This will not modify the original value
# Creating an instance of Example class
obj = Example("original")
print("Before function call:", obj.value)
# Passing the object to the function
modify_value(obj)
print("After function call:", obj.value)  # Output will be "modified"
# Example with immutable object
number = 10
print("Before function call:", number)
# Passing the immutable object to the function
modify_immutable(number)
print("After function call:", number)  # Output will still be 10

```

### what is method overloading?
> Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. These methods are called overloaded methods and this is called method overloading. <br>Like other languages (for example, method overloading in C++) do, python does not support method overloading by default. But there are different ways to achieve method overloading in Python. <br>The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. <b> python does not support method overloading by default, but it is possible</b> 

```python
class calculator:
    #way 1
    def product(self,num1,num2= None,num3=None):
        if num1!=None and num2 !=None and num3!=None:
            return num1*num2*num3
        elif num1!= None and num2 != None:
            return num1*num2 
        else: return num1*1
    #way 2
    def summation(self,*nums):
        sum = 1
        for x in nums:
            sum = sum + x
        return sum

c1 = calculator()
x = c1.product(4)
y = c1.product(4,5)
z = c1.product(4,5,6)
print(x,y,z)
p = c1.summation(11,22,33,4,5)
print(p)
```

> Method overloading Using dispatch

```python
from multipledispatch import dispatch 

class calculator:
    @dispatch(int,int)
    def product(self,a,b):
        return a*b
    
    @dispatch(int,int,int)
    def product(self,a,b,c):
       return a*b*c
   
    @dispatch(str,str)
    def product(self,a,b):
       return int(a)*int(b)


c1 = calculator()
c1.product(4,5)
c1.product(4,5,6)
c1.product("4","5") 

```

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

### What is differnece between *info and **info in functional argument?
> *info collects positional arguments into a tuple.<br>
>**info collects keyword arguments into a dictionary.

### What is operator overloading?
> Operator overloading in Python refers to the ability to redefine how operators work for user-defined classes. This means that you can specify how operators like addition (+), subtraction (-), multiplication (*), etc., behave when applied to objects of your custom classes. We must use special function to implement the necessary requirements. 

1. __add__(self, other): Defines behavior for the addition operator +.
2. __sub__(self, other): Defines behavior for the subtraction operator -.
3. __mul__(self, other): Defines behavior for the multiplication operator *.
4. __truediv__(self, other): Defines behavior for the division operator /.
5. __floordiv__(self, other): Defines behavior for the floor division operator //.
6. __mod__(self, other): Defines behavior for the modulo operator %.
7. __pow__(self, other[, modulo]): Defines behavior for the exponentiation operator **.
8. __eq__(self, other): Defines behavior for the equality operator ==.
9. __ne__(self, other): Defines behavior for the inequality operator !=.
10. __lt__(self, other): Defines behavior for the less-than operator <.
11. __le__(self, other): Defines behavior for the less-than-or-equal-to operator <=.
12. __gt__(self, other): Defines behavior for the greater-than operator >.
13. __ge__(self, other): Defines behavior for the greater-than-or-equal-to operator >=.
14. __str__(self): Defines behavior for when str() is called on an instance of the class.
15. __repr__(self): Defines behavior for when repr() is called on an instance of the class.
16. __len__(self): Defines behavior for when len() is called on an instance of the class.
17. __getitem__(self, key): Defines behavior for when an item is retrieved using the index operator [].
18. __setitem__(self, key, value): Defines behavior for when an item is assigned using the index operator [].
19. __delitem__(self, key): Defines behavior for when an item is deleted using the index operator [].
20. __iter__(self): Returns an iterator object.
21. __next__(self): Retrieves the next item from the iterator.
22. __contains__(self, item): Defines behavior for membership test operators like in and not in.

<img src="../../../public/images/class/operator_overloading.jpg" alt="operator_overloading" width="300" height="200">
<br>
<img src="../../../public/images/class/operator_overloading_2.jpg" alt="operator_overloading" width="300" height="200">

```python
class data: 
    def __init__(self, x):
        self.x = x 
    def __add__(self,other):
        return self.x + other.x 
    def __sub__(self, other):
        return self.x - other.x 
    
num1 = data(12)
num2 = data(34)
print(num1+num2)
print(num1-num2)
```

<b>Real Life Example</b>

```python
class Home:
    def __init__(self,window,door):
        self.window = window
        self.door = door 
    
    def view(self):
        return f"total door = {self.door} and total window = {self.window}"
    def __add__(self,other):
        total_windows = self.window + other.window 
        total_doors = self.door + other.door   
        return f"total door {total_doors} and total window {total_windows}"

h1 = Home(12,22)
h2 = Home(33,444)
print(h1.view())
print(h2.view())
print(h1+h2)

```