import geometry


def circle_area(radius):
    return geometry.pi * radius * radius

def circle_perimeter(radius):
    return 2 * geometry.pi * radius




def square_area(side):
    return side * side

def square_perimeter(side):
    return 4 * side




def rectangle_area(length, breadth):
    return length * breadth

def rectangle_perimeter(length, breadth):
    return 2 * (length + breadth)