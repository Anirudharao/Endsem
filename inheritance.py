class Shape:
    count = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Shape.count += 1

class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

class Circle(Shape):
    def __init__(self, radius=1, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius
        self.count = 69


sq = Square()
print(sq.side)

circle = Circle()
print(circle.radius)
print(circle.count)

print(Shape.count)

"""
database
import
regex
"""