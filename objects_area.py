import math
print("enter the dimensions for the trapezium")
a=float(input("enter base a:"))
b=float(input("enter base b"))
h=float(input("enter height h"))
print("\n enter radius for the circle:")
r=float(input("radius r:"))
area_trapezium=0.5*(a+b)*h
area_circle=math.pi*r**2
shaded_area=area_trapezium-area_circle
print("\n...area calculation...")
print(f"area of trapezium:{area_trapezium:}sq units")
print(f"area of circle:{area_circle:}sq units")
print(f"area of shaded region:{shaded_area}sq units")