import math

class Square:
  def area(self, side):
    result = side**2
    return result

  def diagonal(self, side):
    result = math.sqrt(2) * side
    return result

  def perimeter(self, side):
    result = 4 * side
    return result

  def side(self, area):
    result = math.sqrt(area)
    return result
    
# square = Square()

# print(square.area(2))
# print(square.diagonal(2))
# print(square.perimeter(2))
# print(square.side(2))