def gcd1(num1, num2):
    num = [num1, num2]
    division = 0
    result = 1

    while(division != 1):
        for i in range(1, max(num)):
            if (num[0] % i == 0 and num[1] % i == 0):
                division = i
                if (i == 1):
                    continue
                result = result * division
                num[0] = int(num[0] / i)
                num[1] = int(num[1] / i)
                break

    return result

def get_divisor(num):
    result = []
    
    for i in range(1, num):
        if (num % i == 0):
            result.append(i)
    
    return result

def gcd2(num1, num2):
    divisor1 = set(get_divisor(num1))
    divisor2 = set(get_divisor(num2))
    return max(divisor1.intersection(divisor2))

print(gcd1(280, 30))
print(gcd2(280, 30))