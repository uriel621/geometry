import math

class Cube (object):

    # def __init__(self, edge = 0, surface_area = 0):
    #     self._edge = edge
    #     self._surface_area = surface_area
    
    def diagonal(self, edge_a):
        result = math.sqrt(3)
        result = result * edge_a
        return result
    
    def edge(self, surface_area):
        result = surface_area / 6
        result = math.sqrt(result)
        return result

    def surface_area(self, edge_a):
        result = 6 * edge_a**2
        return result

    def volume(self, edge_a):
        result = edge_a**3
        return result

# cube = Cube(edge=3, surface_area=300)
# diagonal = cube.diagonal()
# edge = cube.edge()
# surface_area = cube.surface_area()
# volume = cube.volume()


# print('diagonal: ', diagonal)
# print('edge: ', edge)
# print('surface_area: ', surface_area)
# print('volume: ', volume)