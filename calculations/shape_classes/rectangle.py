import math

class Rectangle:
  def area(self, width, lenght):
    return width * lenght
  
  def diagonal(self, width, length):
    result = math.sqrt(width**2 + length**2)
    return result
  
  def length(self, area, width):
    result = area / width
    return result

  def perimeter(self, width, length):
    result = 2 * (length + width)
    return result
    
  def width(self, area, length):
    result = area / length
    return result
    
# rectangle = Rectangle()

# print(rectangle.area(2, 3))
# print(rectangle.diagonal(2, 3))
# print(rectangle.length(2, 3))
# print(rectangle.perimeter(2, 3))
# print(rectangle.width(2, 3))