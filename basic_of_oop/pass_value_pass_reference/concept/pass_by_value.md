### what is pass by value?  

>In Python, when you pass an argument to a function, whether it's within an object-oriented context or not, it behaves as if it's passed by object reference. This means that the reference to the object is passed to the function rather than a copy of the object itself.However, it's important to understand that objects themselves can be mutable or immutable. When you pass an immutable object (like integers, strings, or tuples) to a function, it behaves like pass by value because the function cannot modify the original object. When you pass a mutable object (like lists or dictionaries), changes made to the object within the function are reflected in the original object as well.

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

