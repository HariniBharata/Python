class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self,length=0):
        self.length = length
    def area(self):
        print("Area is "+str(self.length*self.length))

s = Square()
s.area()
s1 = Square(10)
s1.area()
        
