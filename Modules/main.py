from math_operations import calculator
from math_operations import geometry

result = calculator.add(10, 20)
print("Addition result:", result)

result = calculator.subtract(888, 666)
print("Subtraction result:", result)


result = geometry.area_cir(3)
print("the area of a circle with radius 3 is", result)

result = geometry.area_tri(3,4)
print("the area of the triangle is:", result)

result = geometry.area_rec(5,8)
print("the area of the rectangle is:", result)