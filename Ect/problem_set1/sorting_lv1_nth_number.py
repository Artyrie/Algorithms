def solution(array, commands):
    # 100점, t7, 0.01ms
    answer = []

    for i, j, n in commands:
        answer.append(sorted(array[i - 1:j])[n - 1])
    return answer