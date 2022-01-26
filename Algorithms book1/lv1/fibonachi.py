def fibonacci(num):
    result = [1, 2]
    if (num <= 0):
        return []
    elif (num == 1):
        return result[:1]
    else:
        for _ in range(num - 2):
            result.append(sum(result[-2:]))
        return result

print(fibonacci(2))