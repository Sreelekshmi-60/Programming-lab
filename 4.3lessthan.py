class Rectangle:
    def __init__(self,length,breadth):
        self.__l=length
        self.__b=breadth
    def __lt__(self,other):
        if(self.area()<other.area()):
            return "Area of rect1 is less than rect2"
        else:
            return "Area of rect2 is less than rect1"
    def area(self):
        return self.__l*self.__b
rect1=Rectangle(5,7)
rect2=Rectangle(12,4)
print("Area of rect1 = ",rect1.area())
print("Area of rect2 = ",rect2.area())
print(rect1<rect2)
