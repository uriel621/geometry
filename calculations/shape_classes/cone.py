import math

class Cone(object):
        
    # def __init__(self, radius=0, surface_area=0, height=0):
    #     self._radius = radius
    #     self._surface_area = surface_area
    #     self._height = height

    def base_area(self, radius):
        result = math.pi * radius**2
        return result

    def height(self, surface_area, radius):
        result = (surface_area / (math.pi * radius) - radius)
        result = result**2 
        result = result - radius**2
        try:
            if math.sqrt(result) > 0:
                return math.sqrt(result)
        except:
            return False
    def lateral_surface(self, radius, height):
        result = height**2 + radius**2
        result = math.sqrt(result)
        result = math.pi * radius * result
        return result

    def radius(self, surface_area, height):
        result = math.pi * height**2 + (2 * surface_area)
        result = math.pi * result
        result = surface_area**2 / result
        result = math.sqrt(result)
        return result

    def slant_height(self, radius, height):
        result = radius**2 + height**2
        result = math.sqrt(result)
        return result

    def surface_area(self, radius, height):
        result = height**2 + radius**2
        result = math.sqrt(result)
        result = radius + result
        result = math.pi * radius * result
        return result

    def volume(self, radius, height):
        result = math.pi * radius**2
        result = result * height / 3
        return result

# cone = Cone(radius=3, surface_area=300, height=10)
# base_area = cone.base_area()
# height = cone.height()
# lateral_surface = cone.lateral_surface()
# radius = cone.radius()
# slant_height = cone.slant_height()
# surface_area = cone.surface_area()
# volume = cone.volume()

# print('base_area: ', base_area)
# print('height: ', height)
# print('lateral_surface: ', lateral_surface)
# print('radius: ', radius)
# print('slant_height: ', slant_height)
# print('surface_area: ', surface_area)
# print('volume: ', volume)