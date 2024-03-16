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
