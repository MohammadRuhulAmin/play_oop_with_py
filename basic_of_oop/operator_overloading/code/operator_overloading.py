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