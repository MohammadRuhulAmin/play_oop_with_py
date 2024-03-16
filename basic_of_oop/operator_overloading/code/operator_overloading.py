class Home:
    def __init__(self,window,door):
        self.window = window
        self.door = door 
    
    def view(self):
        return f"total door = {self.door} and total window = {self.window}"
    def __add__(self,other):
        total_windows = self.window + other.window 
        total_doors = self.door + other.door   
        return Home(total_doors,total_windows)
        #return f"total door {total_doors} and total window {total_windows}"

h1 = Home(12,22)
h2 = Home(33,444)
print(h1.view())
print(h2.view())
h3 = h1+h2
print(h3.view())