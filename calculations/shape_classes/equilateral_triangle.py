import math

class Equilateral_triangle:
    # def __init__(self, side=0):
    #     self._side = side

    def area(self, side):
        result = (math.sqrt(3) / 4) * (side**2)
        return result

    def perimeter(self, side):
        result = 3 * side
        return result

# equilateral_triangle = Equilateral_triangle(side = 2)

# area = equilateral_triangle.area()
# perimeter = equilateral_triangle.perimeter()

# print(area)
# print(perimeter)