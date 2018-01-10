import math

class Heptagon:
    # def __init__(self, side=0, area=0):
    #     self._side = side
    #     self._area = area

    def area(self, side):
        result = side**2 / math.tan(math.pi / 7)
        result = 7 / 4 * result
        return result

    def perimeter(self, side):
        result = 7 * side
        return result

    def side(self, area):
        result = math.tan(math.pi / 7) / 7
        result = math.sqrt(4 * area * result)
        return result

# heptagon = Heptagon(side = 2, area=3)

# area = heptagon.area()
# perimeter = heptagon.perimeter()
# side = heptagon.side()

# print(area)
# print(perimeter)
# print(side)