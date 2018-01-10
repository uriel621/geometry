import sys
import math

class Ellipse (object):

    # def __init__(self, axis_a = 0, axis_b = 0, area=0):
    #     self._axis_a = axis_a
    #     self._axis_b = axis_b
    #     self._area = area

    def area(self, axis_a, axis_b):
        result = math.pi * axis_a * axis_b
        return result
    
    def axis_a(self, area, axis_b):
        result = math.pi * axis_b
        result = area / result
        return result

    def axis_b(self, area, axis_a):
        result = math.pi * axis_a
        result = area / result
        return result

    def circumference(self, axis_a, axis_b):
        result = math.pi * ( 3*(axis_a + axis_b) - math.sqrt( (3 * axis_a + axis_b) * (axis_a + 3 * axis_b) ) )
        return result

# ellipse = Ellipse(axis_a = 3, axis_b = 2, area=5)

# area = ellipse.area()
# axis_a = ellipse.axis_a()
# axis_b = ellipse.axis_b()
# circumference = ellipse.circumference()

# print('area: ', area)
# print('axis_a: ', axis_a)
# print('axis_b: ', axis_b)
# print('circumference: ', circumference)