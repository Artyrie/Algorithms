def check_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def check_ps_prime(num):
    tmp = str(num)
    for i in range(1, len(tmp)):
        if not(check_prime(int(tmp[:-len(tmp) + i]))):
            return False
    return True


def find_sp_prime(digit):
    result = []
    for i in range(10 ** (digit - 1), 10 ** digit):
        if check_ps_prime(i) and check_prime(i):
            result.append(i)
    return result


def main():
    testcase = 1
    while testcase != 0:
        testcase = int(input("1 ~ 8사이의 숫자를 입력하시오 [0: 정지] : "))
        if testcase == 0:
            break
        result = find_sp_prime(testcase)
        print(f"{len(result)}개 ({result}")
    return 0


main()
