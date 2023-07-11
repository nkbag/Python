import logging
import argparse

FORMAT = "{levelname} - {asctime} - {funcName}: {msg}"

logging.basicConfig(format=FORMAT, style="{", filename='сheck.log', level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        print('Треугольник существует')
        logger.info(f'Треугольник {a}/{b}/{b} существует')
        if a == b == c:
            print('Треугольник равносторонний')
            logger.info(f'Треугольник {a}/{b}/{b} равносторонний')
        elif a == b or b == c or c == a:
            print('Треугольник равнобедренный')
            logger.info(f'Треугольник {a}/{b}/{b} равнобедренный')

        else:
            print('Треугольник разносторонний')
            logger.info(f'Треугольник {a}/{b}/{b} разносторонний')
    else:
        print('Такого треугольника не существует')
        logger.error(f'Треугольника {a}/{b}/{b} не существует')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Проверка треугольника")
    parser.add_argument("param", metavar="a b c", type=int, nargs=3, help="Введите a b c через пробел")
    args = parser.parse_args()
    check_triangle(*args.param)
