### what is method overloading?
> Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. These methods are called overloaded methods and this is called method overloading. <br>Like other languages (for example, method overloading in C++) do, python does not support method overloading by default. But there are different ways to achieve method overloading in Python. <br>The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method. <b> python does not support method overloading by default, but it is possible</b> 

```python
class calculator:
    def product(self,num1,num2= None,num3=None):
        if num1!=None and num2 !=None and num3!=None:
            return num1*num2*num3
        elif num1!= None and num2 != None:
            return num1*num2 
        else: return num1*1
       
c1 = calculator()
x = c1.product(4)
y = c1.product(4,5)
z = c1.product(4,5,6)
print(x,y,z)
```