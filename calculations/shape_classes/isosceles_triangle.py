import math

class Isosceles_triangle:
    # def __init__(self, height=0, base=0, area=0, side_a=0, side_c=0, gamma=0):
    #     self._height = height
    #     self._base = base
    #     self._area = area
    #     self._side_a = side_a
    #     self._side_c = side_c
    #     self._gamma = gamma

    def area(self, height, base):
        result = height * base / 2
        return result

    def base(self, area, height):
        result = 2 * area / height
        return result

    def height(self, area, base):
        result = 2 * area / base
        return result

    def perimeter(self, side_a, base_b, side_c):
        result = side_a + base_b + side_c
        return result

    def side(self, area, base, gamma):
        result = 2 * area  / (base * math.sin(math.radians(gamma)))
        return result

# isosceles_triangle = Isosceles_triangle(height=3, base=4, area=5, side_a=6, side_c=7, gamma=8)

# print(isosceles_triangle.area())
# print(isosceles_triangle.base())
# print(isosceles_triangle.height())
# print(isosceles_triangle.perimeter())
# print(isosceles_triangle.side())

