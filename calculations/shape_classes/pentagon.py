import math

class Pentagon(object):
    
  def area(self, side):
    result = math.sqrt(5 * (5 + 2 * math.sqrt(5)))
    result = result * side**2
    result = 1 / 4 * result
    return result
    
  def diagonal(self, side):
    result = (1 + math.sqrt(5)) * (side / 2)
    return result
  
  def perimeter(self, side):
    result = 5 * side
    return result
    
  # def side(self, area): bing vs goog
  #   result = math.sqrt(area) / 5 * (math.sqrt(20) + 5)**.25
  #   result = 2 * 5**.75 * result
  #   return result
    
    
# pentagon = Pentagon()

# print(pentagon.area(2))
# print(pentagon.diagonal(2))
# print(pentagon.perimeter(2))
# print(pentagon.side(20))
