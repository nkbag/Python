class Exceptions(Exception):
    pass


class LongError(Exceptions):

    def __init__(self, param, val):
        self.param = param
        self.val = val

    def __str__(self):

        if self.param < self.val:
            return f'Сторона треугольника не может быть отрицательной\n'
        elif self.param == self.val:
            return f'Сторона треугольника не может быть равна нулю\n'


class TriangleError(Exceptions):

    def __init__(self, val_1: int, val_2: int, val_3: int):
        self.a = val_1
        self.b = val_2
        self.c = val_3

    def __str__(self):
        print(f"Tреугольника со сторонами {self.a}, {self.b}, {self.c} не существует!")
