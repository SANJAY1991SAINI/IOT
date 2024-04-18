# Write a Python Program find an area of a rectangle and perimeter of the rectangle.

len= float(input("Enter length of rectangle: "))
br= float(input("Enter breadth of rectangle: "))

area = len*br
perimeter= 2*(len+br)

print(f"Area of rectangle= {area}")
print(f"Perimeter of rectangle= {perimeter}")