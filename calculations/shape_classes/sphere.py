import math

class Sphere:
  def diameter(self, radius):
    result = 2 * radius
    return result

  def radius(self, surface_area):
    result = 1 / 2 * math.sqrt(surface_area / math.pi)
    return result

  def surface_area(self, radius):
    result = 4 * math.pi * radius**2
    return result

  def volume(self, radius):
    result = 4 * math.pi * radius**3 / 3 
    return result
    
    
# sphere = Sphere()

# print(sphere.diameter(2))
# print(sphere.radius(2))
# print(sphere.surface_area(2))
# print(sphere.volume(2))