square=lambda a:a*a
rectangle=lambda l,b:l*b
triangle=lambda b,h:0.5*b*h
x=float(input("Enter a side of square :"))
length=float(input("Enter length of rectangle :"))
breadth=float(input("Enter breadth of rectangle :"))
base=float(input("Enter base of triangle :"))
height=float(input("Enter height of triangle :"))
print("Area of square having ",x,"= ",square(x))
print("Area of rectangle having length",length," and breadth ",breadth," = ",rectangle(length,breadth))
print("Area of triangle with base",base," and height",height," =",triangle(base,height))