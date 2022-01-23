def fibonacci(num):
    result = [1, 2]
    if (num <= 0):
        return []
    elif (num == 1):
        return result[:1]
    elif (num == 2):
        return result
    else:
        num1 = result[0]
        num2 = result[1]
        tmp = 0
        for _ in range(num - 2):
            # result.append(sum(result[-2:]))
            tmp = num1 + num2
            result.append(tmp)
            num1 = num2
            num2 = tmp
        return result

print(fibonacci(24))