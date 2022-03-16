import itertools
import math


def is_prime_number(num):
    # 100점, t12, max 2162.95ms -> 5.47ms
    if num < 2:
        return False
    else:
        #for i in range(2, num): # 100점, t12, max 2162.95ms
        #for i in range(2, math.ceil((math.sqrt(num)))): # 75점, t9 => 제곱수일 경우 range 범위에 root(n)이 제외됨
        for i in range(2, int(math.sqrt(num)) + 1): # 100점, t12, max 5.47ms
            if num % i == 0:
                return False
    return True


def eratos(num):
    # 100점, t12, max 5250.90ms
    result = [True] * (num + 1)
    result[0] = False
    result[1] = False

    for i in range(2, num + 1):
        if result[i]:
            ctr = 2
            while i * ctr <= num:
                result[i * ctr] = False
                ctr += 1
    return result


def solution(numbers):
    answer = 0
    pool = [numbers[i] for i in range(len(numbers))]
    number = []
    for i in range(1, len(pool) + 1):
        number.extend(list(map(''.join, itertools.permutations(pool, i))))

    number = list(set(map(int, number)))
    #prime = eratos(int(len(numbers) * '9'))

    for val in number:
        if is_prime_number(int(val)):
        #if prime[val]:
            answer += 1
    return answer


print(solution('17'))