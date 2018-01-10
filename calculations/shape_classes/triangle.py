import math

class Triangle:
  def area(self, height, base):
    result = base / 2
    result = height * result
    return result
    
  def base(self, area, height):
    result = area / height
    result = 2 * result
    return result
    
  def height(self, area, base_b):
    result = area / base_b
    result = 2 * result
    return result

  def perimeter(self, base_a, base_b, side_c):
    result = base_a + base_b + side_c
    return result

  def side_a(self, area, base_b, gamma):
    result = base_b * math.sin(math.radians(gamma))
    result = area / result
    result = 2 * result
    return result
    
  def side_c(self, perimeter, base_a, base_b):
    result = perimeter - base_a - base_b
    return result
    
# triangle = Triangle()

# print(triangle.area(2, 3))
# print(triangle.base(2, 3))
# # print(triangle.gamma(555, 555, 555))
# print(triangle.height(2, 3))
# print(triangle.perimeter(2, 3, 4))
# print(triangle.side_a(2, 3, 4))
# print(triangle.side_c(2, 3, 4))
