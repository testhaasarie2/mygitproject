import math

diameter = input("Provide the diameter:\n\n")

diameter_num = float(diameter)
radius       = diameter_num / 2
circle = math.pow(radius, 2) * math.pi

circle_double = circle * 2
print(f"You inserted the diameter" {circle_double}\n") # <-- extra print statement
print(f"\nResult: {round(circle, 2)}\n")
print(f"\The double circle is: {round(circle, 2)}\n")