import math

class Pyramid(object):
  def base_area(self, width, length):
    result = width * length
    return result
    
  def base_length(self, base_area, width):
      result = base_area / width
      return result
    
  def base_width(self, base_area, length):
      result = base_area / length
      return result  
      
  def height(self, volume, width, length):
      result = 3 * volume / (width * length)
      return result  

  def lateral_surface(self, width, length, height):
      left = length * math.sqrt((width / 2)**2 + height**2)
      right = width * math.sqrt((length / 2)**2 + height**2)
      return left + right
    
  def surface_area(self, width, length, height):
      left = length * width 
      middle = length * math.sqrt((width / 2)**2 + height**2)
      right = width * math.sqrt((length / 2)**2 + height**2)
      return left + middle + right
  
  def volume(self, width, length, height):
      result = length * width * height / 3
      return result    
      
# pyramid = Pyramid()

# print(pyramid.base_area(2, 3))
# print(pyramid.base_length(2, 3))
# print(pyramid.base_width(2, 3))
# print(pyramid.height(2, 3, 4))
# print(pyramid.lateral_surface(2, 3, 4))
# print(pyramid.surface_area(2, 3, 4))
# print(pyramid.volume(2, 3, 4))