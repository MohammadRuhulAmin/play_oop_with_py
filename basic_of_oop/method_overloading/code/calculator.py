class calculator:
    # way 1
    def product(self,num1,num2= None,num3=None):
        if num1!=None and num2 !=None and num3!=None:
            return num1*num2*num3
        elif num1!= None and num2 != None:
            return num1*num2 
        else: return num1*1
    # way 2
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