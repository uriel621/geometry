from calculations.shape_classes.circle import Circle
from calculations.shape_classes.cone import Cone
from calculations.shape_classes.cube import Cube
from calculations.shape_classes.cylinder import Cylinder
from calculations.shape_classes.ellipse import Ellipse
from calculations.shape_classes.equilateral_triangle import Equilateral_triangle
from calculations.shape_classes.heptagon import Heptagon
from calculations.shape_classes.hexagon import Hexagon
from calculations.shape_classes.isosceles_triangle import Isosceles_triangle
from calculations.shape_classes.octagon import Octagon
from calculations.shape_classes.octahedron import Octahedron
from calculations.shape_classes.parallelogram import Parallelogram
from calculations.shape_classes.pentagon import Pentagon
from calculations.shape_classes.pyramid import Pyramid
from calculations.shape_classes.rectangle import Rectangle
from calculations.shape_classes.rhombus import Rhombus
from calculations.shape_classes.right_triangle import Right_triangle
from calculations.shape_classes.sphere import Sphere
from calculations.shape_classes.square import Square
from calculations.shape_classes.tetrahedron import Tetrahedron
from calculations.shape_classes.trapezoid import Trapezoid
from calculations.shape_classes.triangle import Triangle

def circle(formula, pairs):
    result = None
    circle = Circle()
    if formula == 'area':
        result = circle.area(pairs['radius_r'])
    elif formula == 'circumference':
        result = circle.circumference(pairs['radius_r'])
    elif formula == 'diameter':
        result = circle.diameter(pairs['radius_r'])
    elif formula == 'radius':
        result = circle.radius(pairs['area_A'])
    return round(result, 3)

def cone(formula, pairs):
    result = None
    cone = Cone()
    if formula == 'base_area':
        result = cone.base_area(pairs['radius_r'])
    elif formula == 'height':
        result = cone.height(pairs['surface_area'], pairs['radius_r'])
        if result == False:
            return '?'
    elif formula == 'lateral_surface':
        result = cone.lateral_surface(pairs['radius_r'], pairs['height_h'])
    elif formula == 'radius':
        result = cone.radius(pairs['surface_area'], pairs['height_h'])
    elif formula == 'slant_height':
        result = cone.slant_height(pairs['radius_r'], pairs['height_h'])
    elif formula == 'surface_area':
        result = cone.surface_area(pairs['radius_r'], pairs['height_h'])
    elif formula == 'volume':
        result = cone.volume(pairs['radius_r'], pairs['height_h'])
    return round(result, 3)

def cube(formula, pairs):
    result = None
    cube = Cube()
    if formula == 'diagonal':
        result = cube.diagonal(pairs['edge_a'])
    elif formula == 'edge':
        result = cube.edge(pairs['surface_area'])
    elif formula == 'surface_area':
        result = cube.surface_area(pairs['edge_a'])
    elif formula == 'volume':
        result = cube.volume(pairs['edge_a'])
    return round(result, 3)

def cylinder(formula, pairs):
    result = None
    cylinder = Cylinder()
    if formula == 'base_area':
        result = cylinder.base_area(pairs['radius_r'])
    elif formula == 'height':
        result = cylinder.height(pairs['area_A'], pairs['radius_r'])
    elif formula == 'lateral_surface':
        result = cylinder.lateral_surface(pairs['radius_r'], pairs['height_h'])
    elif formula == 'radius':
        result = cylinder.radius(pairs['surface_area'], pairs['height_h'])
    elif formula == 'surface_area':
        result = cylinder.surface_area(pairs['radius_r'], pairs['height_h'])
    elif formula == 'volume':
        result = cylinder.volume(pairs['radius_r'], pairs['height_h'])
    return round(result, 3)

def ellipse(formula, pairs):
    result = None
    ellipse = Ellipse()
    if formula == 'area':
        result = ellipse.area(pairs["axis_a"], pairs["axis_b"])
    elif formula == 'axis_a':
        result = ellipse.axis_a(pairs["area_A"], pairs["axis_b"])
    elif formula == 'axis_b':
        result = ellipse.axis_b(pairs["area_A"], pairs["axis_a"])
    elif formula == 'circumference':
        result = ellipse.circumference(pairs["axis_a"], pairs["axis_b"])
    return round(result, 3)

def equilateral_triangle(formula, pairs):
    result = None
    equilateral_triangle = Equilateral_triangle()
    if formula == 'area':
        result = equilateral_triangle.area(pairs["side_a"])
    elif formula == 'perimeter':
        result = equilateral_triangle.perimeter(pairs["side_a"])
    return round(result, 3)

def heptagon(formula, pairs):
    result = None
    heptagon = Heptagon()
    if formula == 'area':
        result = heptagon.area(pairs["side_a"])
    elif formula == 'perimeter':
        result = heptagon.perimeter(pairs["side_a"])
    elif formula == 'side':
        result = heptagon.side(pairs["area_A"])
    return round(result, 3)

def hexagon(formula, pairs):
    result = None
    hexagon = Hexagon()
    if formula == 'area':
        result = hexagon.area(pairs["side_a"])
    elif formula == 'perimeter':
        result = hexagon.perimeter(pairs["side_a"])
    elif formula == 'side':
        result = hexagon.side(pairs["area_A"])
    return round(result, 3)

def isosceles_triangle(formula, pairs):
    result = None
    isosceles_triangle = Isosceles_triangle()
    if formula == 'area':
        result = isosceles_triangle.area(pairs["height_h"], pairs["base_b"])
    elif formula == 'base':
        result = isosceles_triangle.base(pairs["area_A"], pairs["height_h"])
    elif formula == 'height':
        result = isosceles_triangle.height(pairs["area_A"], pairs["base_b"])
    elif formula == 'perimeter':
        result = isosceles_triangle.perimeter(pairs["side_a"], pairs["base_b"], pairs["side_c"])
    elif formula == 'side':
        result = isosceles_triangle.side(pairs["area_A"], pairs["base_b"], pairs["gamma_y"])
    return round(result, 3)

def octagon(formula, pairs):
    result = None
    octagon = Octagon()
    if formula == 'area':
        result = octagon.area(pairs["side_a"])
    elif formula == 'perimeter':
        result = octagon.perimeter(pairs["side_a"])
    elif formula == 'side':
        result = octagon.side(pairs["area_A"])
    return round(result, 3)

def octahedron(formula, pairs):
    result = None
    octahedron = Octahedron()
    if formula == 'surface_area':
        result = octahedron.surface_area(pairs["edge_a"])
    elif formula == 'volume':
        result = octahedron.volume(pairs["edge_a"])
    return round(result, 3)

def parallelogram(formula, pairs):
    result = None
    parallelogram = Parallelogram()
    if formula == 'area':
        result = parallelogram.area(pairs["base_b"], pairs["height_h"])
    elif formula == 'base':
        result = parallelogram.base(pairs["area_A"], pairs["height_h"])
    elif formula == 'height':
        result = parallelogram.height(pairs["area_A"], pairs["base_b"])
    elif formula == 'perimeter':
        result = parallelogram.perimeter(pairs["side_a"], pairs["base_b"])
    elif formula == 'side':
        result = parallelogram.side(pairs["perimeter_P"], pairs["base_b"])
    return round(result, 3)

def pentagon(formula, pairs):
    result = None
    pentagon = Pentagon()
    if formula == 'area':
        result = pentagon.area(pairs["side_a"])
    elif formula == 'diagonal':
        result = pentagon.diagonal(pairs["side_a"])
    elif formula == 'perimeter':
        result = pentagon.perimeter(pairs["side_a"])
    return round(result, 3)

def pyramid(formula, pairs):
    result = None
    pyramid = Pyramid()
    if formula == 'base_area':
        result = pyramid.base_area(pairs["width_w"], pairs["length_l"])
    elif formula == 'base_length':
        result = pyramid.base_length(pairs["base_area"], pairs["width_w"])
    elif formula == 'base_width':
        result = pyramid.base_width(pairs["base_area"], pairs["length_l"])
    elif formula == 'height':
        result = pyramid.height(pairs["volume_V"], pairs["width_w"], pairs["length_l"])
    elif formula == 'lateral_surface':
        result = pyramid.lateral_surface(pairs["width_w"], pairs["length_l"], pairs["height_h"])
    elif formula == 'surface_area':
        result = pyramid.surface_area(pairs["width_w"], pairs["length_l"], pairs["height_h"])
    elif formula == 'volume':
        result = pyramid.volume(pairs["width_w"], pairs["length_l"], pairs["height_h"])
    return round(result, 3)

def rectangle(formula, pairs):
    result = None
    rectangle = Rectangle()
    if formula == 'area':
        result = rectangle.area(pairs["width_w"], pairs["length_l"])
    elif formula == 'diagonal':
        result = rectangle.diagonal(pairs["width_w"], pairs["length_l"])
    elif formula == 'length':
        result = rectangle.length(pairs["area_A"], pairs["width_w"])
    elif formula == 'perimeter':
        result = rectangle.perimeter(pairs["width_w"], pairs["length_l"])
    elif formula == 'width':
        result = rectangle.width(pairs["area_A"], pairs["length_l"])
    return round(result, 3)

def rhombus(formula, pairs):
    result = None
    rhombus = Rhombus()
    if formula == 'area':
        result = rhombus.area(pairs["diagonal_p"], pairs["diagonal_q"])
    elif formula == 'diagonal_p':
        result = rhombus.diagonal_p(pairs["area_A"], pairs["diagonal_q"])
    elif formula == 'diagonal_q':
        result = rhombus.diagonal_q(pairs["area_A"], pairs["diagonal_p"])
    elif formula == 'perimeter':
        result = rhombus.perimeter(pairs["side_a"])
    elif formula == 'side':
        result = rhombus.side(pairs["diagonal_p"], pairs["diagonal_q"])
    return round(result, 3)

def right_triangle(formula, pairs):
    result = None
    right_triangle = Right_triangle()
    if formula == 'area':
        result = right_triangle.area(pairs["side_a"], pairs["base_b"])
    elif formula == 'base':
        result = right_triangle.base(pairs["hypotenuse_c"], pairs["gamma_y"])
    elif formula == 'hypotenuse':
        result = right_triangle.hypotenuse(pairs["side_a"], pairs["base_b"])
    elif formula == 'perimeter':
        result = right_triangle.perimeter(pairs["side_a"], pairs["base_b"], pairs["hypotenuse_c"])
    elif formula == 'side':
        result = right_triangle.side(pairs["hypotenuse_c"], pairs["gamma_y"])
    return round(result, 3)

def sphere(formula, pairs):
    result = None
    sphere = Sphere()
    if formula == 'diameter':
        result = sphere.diameter(pairs["radius_r"])
    elif formula == 'radius':
        result = sphere.radius(pairs["surface_area"])
    elif formula == 'surface_area':
        result = sphere.surface_area(pairs["radius_r"])
    elif formula == 'volume':
        result = sphere.volume(pairs["radius_r"])
    return round(result, 3)

def square(formula, pairs):
    result = None
    square = Square()
    if formula == 'area':
        result = square.area(pairs["side_a"])
    elif formula == 'diagonal':
        result = square.diagonal(pairs["side_a"])
    elif formula == 'perimeter':
        result = square.perimeter(pairs["side_a"])
    elif formula == 'side':
        result = square.side(pairs["area_A"])
    return round(result, 3)

def tetrahedron(formula, pairs):
    result = None
    tetrahedron = Tetrahedron()
    if formula == 'edge':
        result = tetrahedron.edge(pairs["surface_area"])
    elif formula == 'face_area':
        result = tetrahedron.face_area(pairs["edge_a"])
    elif formula == 'height':
        result = tetrahedron.height(pairs["edge_a"])
    elif formula == 'surface_area':
        result = tetrahedron.surface_area(pairs["edge_a"])
    elif formula == 'volume':
        result = tetrahedron.volume(pairs["edge_a"])
    return round(result, 3)


def trapezoid(formula, pairs):
    result = None
    trapezoid = Trapezoid()
    if formula == 'area':
        result = trapezoid.area(pairs["base_a"], pairs["base_b"], pairs["height_h"])
    elif formula == 'base_a':
        result = trapezoid.base_a(pairs["area_A"], pairs["base_b"], pairs["height_h"])
    elif formula == 'base_b':
        result = trapezoid.base_b(pairs["area_A"], pairs["base_a"], pairs["height_h"])
    elif formula == 'height':
        result = trapezoid.height(pairs["base_a"], pairs["base_b"], pairs["area_A"])
    elif formula == 'perimeter':
        result = trapezoid.perimeter(pairs["base_a"], pairs["base_b"], pairs["side_c"], pairs["side_d"])
    elif formula == 'side_c':
        result = trapezoid.side_c(pairs["perimeter_P"], pairs["base_a"], pairs["base_b"], pairs["side_d"])
    elif formula == 'side_d':
        result = trapezoid.side_d(pairs["perimeter_P"], pairs["base_a"], pairs["base_b"], pairs["side_c"])    
    return round(result, 3)

def triangle(formula, pairs):
    result = None
    triangle = Triangle()
    if formula == 'area':
        result = triangle.area(pairs["height_h"], pairs["base_b"])
    elif formula == 'base':
        result = triangle.base(pairs["area_A"], pairs["height_h"])
    elif formula == 'height':
        result = triangle.height(pairs["area_A"], pairs["base_b"])
    elif formula == 'perimeter':
        result = triangle.perimeter(pairs["side_a"], pairs["base_b"], pairs["side_c"])
    elif formula == 'side_a':
        result = triangle.side_a(pairs["area_A"], pairs["base_b"], pairs["gamma_y"])
    elif formula == 'side_c':
        result = triangle.side_c(pairs["perimeter_P"], pairs["side_a"], pairs["side_b"])
    return round(result, 3)