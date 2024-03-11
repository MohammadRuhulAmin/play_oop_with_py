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
    