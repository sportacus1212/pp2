#1
import math
degree = int(input("Input degree: "))
radian = degree * math.pi / 180
print("Output radian:", radian)

#2
height = int(input("Height: "))
base1 = int(input("Base, first value: "))
base2 = int(input("Base, second value: "))
area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)

#3
import math
n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
area = (n * s**2) / (4 * math.tan(math.pi/n))
print("The area of the polygon is:", area)

#4
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = base * height
print("Expected Output:", area)



