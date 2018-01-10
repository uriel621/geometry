class Trapezoid:
  def area(self, base_a, base_b, height):
    result = (base_a + base_b) * height / 2
    return result
    
  def base_a(self, area, base_b, height):
    result = 2 * area / height - base_b
    return result
    
  def base_b(self, area, base_a, height):
    result = 2 * area / height - base_a
    return result    

  def height(self, base_a, base_b, area):
    result = base_a + base_b
    result = area / result
    result = 2 * result
    return result

  def perimeter(self, base_a, base_b, side_c, side_d):
    result = base_a + base_b + side_c + side_d
    return result

  def side_c(self, perimeter, base_a, base_b, side_d):
    result = perimeter - base_a - base_b - side_d
    return result
    
  def side_d(self, perimeter, base_a, base_b, side_c):
    result = perimeter - base_a - base_b - side_c
    return result
    
# trapezoid = Trapezoid()

# print(trapezoid.area(2, 3, 4))
# print(trapezoid.base_a(2, 3, 4))
# print(trapezoid.base_b(2, 3, 4))
# print(trapezoid.height(2, 3, 4))
# print(trapezoid.perimeter(2, 3, 4, 5))
# print(trapezoid.side_c(2, 3, 4, 5))
# print(trapezoid.side_d(2, 3, 4, 5))
