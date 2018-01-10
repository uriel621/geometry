import math

class Parallelogram:
    # def __init__(self, base=0, height=0, area=0, side=0, perimeter=0):
    #     self._base = base 
    #     self._height = height 
    #     self._area = area 
    #     self._side = side
    #     self._perimeter = perimeter

    def area(self, base, height):
        result = base * height
        return result

    def base(self, area, height):
        result = area / height
        return result

    def height(self, area, base):
        result = area / base
        return result
    
    def perimeter(self, side, base):
        result = 2 * (side + base)
        return result
        
    def side(self, perimeter, base):
        result = perimeter / 2 - base
        return result

# octagon = Parallelogram(base=2, height=3, area=4, side=5, perimeter=6)

# print(octagon.area())
# print(octagon.base())
# print(octagon.height())
# print(octagon.perimeter())
# print(octagon.side())