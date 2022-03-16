import math


def solution(brown, yellow):
    # 100점, t13, max 0.12ms
    total = brown + yellow
    divisor = []

    for i in range(2, int(math.sqrt(total)) + 1):
        if total % i == 0:
            divisor.append((int(total / i), i))

    for x, y in divisor[::-1]:
        tmp = (x - 2) * (y - 2)
        if tmp == yellow and tmp == total - brown:
            return [x, y]