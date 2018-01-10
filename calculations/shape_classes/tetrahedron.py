import math

class Tetrahedron:
  def edge(self, surface_area):
    result = 1 / 3 * 3**.75 * math.sqrt(surface_area)
    return result

  def face_area(self, edge):
    result = math.sqrt(3) * edge**2 / 4
    return result

  def height(self, edge):
    result = math.sqrt(2 / 3) * edge
    return result

  def surface_area(self, edge):
    result = math.sqrt(3) * edge**2
    return result

  def volume(self, edge):
    top = edge**3 
    bottom = 6 * math.sqrt(2)
    return top / bottom
    
# tetrahedron = Tetrahedron()

# print(tetrahedron.edge(2))
# print(tetrahedron.face_area(2))
# print(tetrahedron.height(2))
# print(tetrahedron.surface_area(2))
# print(tetrahedron.volume(2))