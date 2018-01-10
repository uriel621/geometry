import math

class Right_triangle:
  
    def area(self, side, base):
      result = side * base / 2
      return result
      
    def base(self, hypotenuse, gamma):
      result = math.cos(math.radians(gamma)) * hypotenuse
      return result
      
    # def gamma(self, side, hypotenuse):
    #   result = side * math.sin(side / hypotenuse)
    #   return result
    
    def hypotenuse(self, side, base):
      result = math.sqrt(side**2 + base**2)
      return result
      
    def perimeter(self, side, base, hypotenuse):
      result = side + base + hypotenuse
      return result
      
    def side(self, hypotenuse, gamma):
      result = math.sin(math.radians(gamma)) * hypotenuse
      return result

# right_triangle = Right_triangle()

# print(right_triangle.area(2, 3))
# print(right_triangle.base(2, 3))
# # print(right_triangle.gamma(2, 3))
# print(right_triangle.hypotenuse(2, 3))
# print(right_triangle.perimeter(2, 3, 4))
# print(right_triangle.side(2, 3))
