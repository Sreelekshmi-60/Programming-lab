class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        return self.l*self.b
    def perimeter(self):
        return 2*(self.l+self.b)
rect1=Rectangle(20,5)
print("Area of rect1 = ",rect1.area())
print("Perimeter of rect1 =",rect1.perimeter())

rect2=Rectangle(16,8)
print("Area of rect2 =",rect2.area())
print("Perimeter of rect2 =",rect2.perimeter())
if(rect1.area()>rect2.area()):
    print("rect1 is bigger than rect2")
else:
    print("rect2 is bigger than rect1")
