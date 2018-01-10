import math

class Octahedron(object):
    # def __init__(self,area=0, edge=0):
    #     self._area = area
    #     self._edge = edge

    # def edge(self):
    #     result = 3**1/4 * math.sqrt(self._area / 18)
    #     return result

    def surface_area(self, edge):
        result = 2 * math.sqrt(3) * edge**2
        return result

    def volume(self, edge):
        result = math.sqrt(2) * edge**3 / 3
        return result

# octagon = Octahedron(area=3, edge=4)

# print(octagon.edge())
# print(octagon.surface_area())
# print(octagon.volume())