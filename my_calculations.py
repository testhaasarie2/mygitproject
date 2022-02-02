import math

diameter = input("Provide the diameter:\n\n")

diameter_num = float(diameter)
radius       = diameter_num / 2
circle = math.pow(radius, 2) * math.pi

print(f"\nResult: {round(circle, 2)}\n")