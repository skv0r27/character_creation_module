import math

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'


def calculate_square_root(numb):
    """Вычисляет квадратный корень."""
    return math.sqrt(numb)


def calc(your_numb):
    """Ваше число."""
    zet = calculate_square_root(your_numb)
    if your_numb <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {zet}')


print(message)
calc(25.5)
