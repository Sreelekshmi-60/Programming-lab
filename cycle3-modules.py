from graphics._3Dgraphics.sphere import sphereperimeter
from graphics._3Dgraphics.sphere import spherearea
from graphics import rectangle
from graphics import circle
from graphics._3Dgraphics import cuboid
r=int(input("Enter radius of circle :"))
circle.circlearea(r)
circle.circleperimeter(r)
l=int(input("Enter length of rectangle :"))
b=int(input("Enter breadth of rectangle :"))
rectangle.rectarea(l,b)
rectangle.rectperimeter(l,b)
spr=int(input("Enter radius of sphere :"))
spherearea(spr)
sphereperimeter(spr)
length=int(input("Enter length of cuboid:"))
breadth=int(input("Enter breadth of cuboid:"))
height=int(input("Enter height of a cuboid :"))
cuboid.cubarea(length,breadth,height)
cuboid.cubperimeter(length,breadth,height)
