from itertools import product


def solution1(numbers, target):
    # 100점, t8 max 2108.21ms
    answer = 0
    oper = [-1, 1]  # 0 : -, 1 : +

    for val in product(oper, repeat=len(numbers)):
        total = 0
        for i in range(len(numbers)):
            total += numbers[i] * val[i]
        if total == target:
            answer += 1
    return answer


def solution2(numbers, target):
    # 100점, t8 max 362.64ms
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution2(numbers[1:], target + numbers[0]) + solution2(numbers[1:], target - numbers[0])
    return answer