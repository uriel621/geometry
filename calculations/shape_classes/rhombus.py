import math

class Rhombus:
  def area(self, diagonal_p, diagonal_q):
    result = diagonal_p * diagonal_q / 2
    return result
    
  def diagonal_p(self, area, diagonal_q):
    result = 2 * area / diagonal_q
    return result

  def diagonal_q(self, area, diagonal_p):
    result = 2 * area / diagonal_p
    return result

  def perimeter(self, side):
    result = 4 * side
    return result
    
  def side(self, diagonal_p, diagonal_q):
    result = math.sqrt(diagonal_p**2 + diagonal_q**2) / 2
    return result
    
# rhombus = Rhombus()

# print(rhombus.area(2, 3))
# print(rhombus.diagonal_p(2, 3))
# print(rhombus.diagonal_p(2, 3))
# print(rhombus.perimeter(2))
# print(rhombus.side(2, 3))