import math

class Hexagon:
    # def __init__(self, side=0, area=0):
    #     self._side = side
    #     self._area = area

    def area(self, side):
        result = 3 * math.sqrt(3) / 2 * side**2
        return result

    def perimeter(self, side):
        result = 6 * side
        return result

    def side(self, area):
        result = area * 2 / (3 * math.sqrt(3))
        result = math.sqrt(result)
        return result

# hexagon = Hexagon(side=2, area=3)

# area = hexagon.area()
# perimeter = hexagon.perimeter()
# side = hexagon.side()

# print(area)
# print(perimeter)
# print(side)