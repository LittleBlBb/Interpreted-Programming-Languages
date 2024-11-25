from argparse import ArgumentTypeError

class Shape:
    x1 = x2 = y1 = y2 = 0

    def __init__(self, a, b):
        self.sides = []
        self.sides.append(a)
        self.sides.append(b)
        Shape.check_sides_for_type_float_int(self)
        self.x2 = self.sides[1]
        self.y2 = self.sides[0]

    def move(self, x, y):
        self.x1 = x
        self.y1 = y
        self.x2 = self.x1 + self.sides[1]
        self.y2 = self.y1 + self.sides[0]

    def check_sides_for_type_float_int(self):
        for side in self.sides:
            if type(side) != int and type(side) != float:
                raise ArgumentTypeError(f"Expected type int or float, given {type(side)}")


    def is_include(self, other):
        if other.x1 >= self.x1 and other.x2 <= self.x2:
            if other.y1 >= self.y1 and other.y2 <= self.y2:
                return True
        return False

    def display(self):
        print(f"x1 = {self.x1} y1 = {self.y1}\n"
              f"x2 = {self.x2} y2 = {self.y2}")

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.sides.append(a)
        self.sides.append(b)

class Pentagon(Shape):
    c = d = e = 0
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b)
        self.sides.append(c)
        self.sides.append(d)
        self.sides.append(e)
        Shape.check_sides_for_type_float_int(self)
        self.x2 = self.sides[1]
        self.y2 = self.sides[0]

rectangle = Rectangle(4,5)
pentagon = Pentagon(1, 2, 3, 4, 5)

print ("Стороны прямоугольника:")
for side in rectangle.sides:
    print(side)

rectangle.display()

print ("Стороны пятиугольника:")
for side in pentagon.sides:
    print(side)

pentagon.display()

print(rectangle.is_include(pentagon))

print(pentagon.is_include(rectangle))