import math
# print(sys.argv[1])

class Circle (object):
    # pi = math.pi
    # def __init__(self, radius = 0, area = 0):
    #     self._radius = radius
    #     self._area = area
    def area(self, radius):
        result = math.pi * radius**2
        return result
    
    def circumference(self, radius):
        result = 2 * math.pi * radius
        return result

    def diameter(self, radius):
        result = 2 * radius
        return result

    def radius(self, area):
        result = area / math.pi
        result = math.sqrt(result)
        return result

# radius = sys.argv[1]
# # area = sys.argv[1]
# radius = float(radius)
# # radius = float(radius)
# radius = Circle(radius, radius)
# print(radius.area())
# print(radius.circumference())
# print(radius.diameter())
# print(radius.radius())