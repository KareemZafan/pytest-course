class Rectangle:
    def __init__(self):
        self.length=5
        self.width=5

    def set_length(self, l):
        self.length = l  

    def set_width(self, w):
        self.width = w  
    
    def get_length(self):
        return self.length 

    def get_width(self):
        self.width = w  
    
    def permieter(self):
        return (self.length + self.width) * 2
    
    def area(self):
        return (self.length * self.width) 
    
