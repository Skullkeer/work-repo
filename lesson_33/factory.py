class Circle:
    def __init__(self, radius):
        self.radius = radius

class Triangle:
    def __init__(self, verticies, perpheight):
        self.verticies = verticies
        self.perpheight = perpheight

class Square:
    def __init__(self, verticies, side_len):
        self.verticies = verticies
        self.side_len = side_len

class ShapeFactory:
    def create_circle(self, radius):
        return Circle(radius)

    def create_triangle(self, height):
        return Triangle(3, height)

    def create_square(self, leng):
        return Square(4, leng)

    def create_rhombus(self):
        t = create_triangle(2)
        s = create_square(4)
        return [t,s]
