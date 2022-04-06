import string
import math

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def is_prime_number(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
    return True


def solution(n, k):
    answer = 0
    if k == 10:
        num = str(n).split('0')
    else:
        num = convert(n, k)
        num = num.split('0')

    for val in num:
        if val == '':
            continue
        else:
            if is_prime_number(int(val)):
                answer += 1
    return answer