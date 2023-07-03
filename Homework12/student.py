# Создайте класс студента. Создайте класс студента. * Используя дескрипторы проверяйте ФИО на первую заглавную букву
# и наличие только букв. * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие
# предметы в экземпляре недопустимы. * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от
# 0 до 100). * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех
# предметов вместе взятых.

import csv
from statistics import mean


def validate(value: str):
    if not value.isalpha():
        raise AttributeError(f'{value} должно содержать только буквы')
    if not value.istitle():
        raise AttributeError(f'{value} должно начинаться с заглавной буквы')


class Names:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, obj_type=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        validate(value)
        setattr(obj, self.private_name, value)


def _load_data():
    data = {}
    file_name = 'subjects.csv'
    i = 0
    with open(file_name, encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        for item in csv_reader:
            res = ''.join(item).strip()
            i += 1
            if i != 1:
                data[res] = None
    return data


def item(value: dict):
    data = _load_data()
    valid = 0
    for d in data:
        for v in value:
            if d == v:
                valid += 1
    if valid != len(value):
        raise AttributeError(f'Предмета нет в списке')


class Validate:

    def __init__(self, min_value: int = None, max_value: int = None):
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, name):
        self.private_item = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_item)

    def __set__(self, obj, value: dict):
        self.gradie(value)
        item(value)

        setattr(obj, self.private_item, value)

    def gradie(self, value: dict):
        for value in value.values():
            for value_tuple in value:
                if not isinstance(value_tuple, int):
                    raise TypeError(f'Значение {value_tuple} должно быть целым числом')
                if value_tuple is not None and value_tuple < self._min_value:
                    raise ValueError(f'Значение {value_tuple} должно быть больше или равно {self._min_value}')
                if value_tuple is not None and value_tuple > self._max_value:
                    raise ValueError(f'Значение {value_tuple} должно быть меньше или равно {self._max_value}')


class Student:
    first_name: str = Names()
    last_name: str = Names()
    grades: dict = Validate(2, 5)
    tests: dict = Validate(0, 100)

    def __init__(self):
        self._first_name: str = ''
        self._last_name: str = ''
        self._grades: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def __str__(self):
        grades = '\n'.join(f'{k}: {v}' for k, v in self._grades.items())
        tests = '\n'.join(f'{k}: {v}' for k, v in self._tests.items())
        result_test = '\n'.join(f'{k}: {v}' for k, v in self._avg_tests().items())
        result_grade = '\n'.join(f'{k}: {v}' for k, v in self._avg_grades().items())
        return f'Студент: {self._first_name} {self._last_name}\n\n' \
               f'Оценки по тестам:\n{tests}\n' \
               f'Оценки по предметам:\n{grades}\n' \
               f'Средняя оценка по тестам:\n{result_test}\n' \
               f'Средняя оценка по всем предметам:\n{result_grade}'

    def _avg_tests(self):
        avg_results = dict()
        for key, value in self._tests.items():
            avg_results[key] = round(mean(value), 1)
        return avg_results

    def _avg_grades(self):
        avg_result = 0
        for values in self._grades.values():
            avg_result += mean(values)
        return {'Средний балл по всем предметам': round(avg_result / len(self._grades.values()), 1)}


if __name__ == '__main__':
    student = Student()
    student.first_name = 'Евгений'
    student.last_name = 'Пригожин'
    student.grades = {'Английский язык': (3, 5, 2, 4, 5), 'История': (4, 3, 5, 4, 3), 'Химия': (2, 4, 2, 5, 5, 4)}
    student.tests = {'Математика': (57, 98), 'Русский язык': (60, 87), 'Физика': (77, 100)}
    print(student)
