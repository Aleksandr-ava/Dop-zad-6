from math import sqrt
import numpy as np

A = np.array([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, ])


class Figure:
    def __init__(self, __color, *__sides):
        self.__sides = __sides
        self.__color = __color
        self.sides_count = 0
        self.filed = False
        self.r = int
        self.g = int
        self.b = int

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def __is_valid_sides(self, args):
        if len(args) == self.sides_count and all(isinstance(side, int) for side in args):
            return True

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *args):
        if self.__is_valid_sides(args) is True:
            self.__sides = args
        else:
            self.__sides = A

    def __len__(self):
        for i in self.__sides:
            return i


class Circle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 1
        self.__radius = sides[0] / 2 * 3.14

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 3
        self.sides = None
        self.__height = self.get_square(sides) * 2 / sides[0]

    def get_square(self, sides):
        self.sides = sides
        p = (sides[0] + sides[1] + sides[2]) / 2
        s = sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        return int('%.2f' % s)


class Cube(Figure):
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides_count = 12
        self.__sides = sides * self.sides_count

    def get_volume(self):
        return self.__sides[0] * self.__sides[1] * self.__sides[2]


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(list(circle1.get_sides()))

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
