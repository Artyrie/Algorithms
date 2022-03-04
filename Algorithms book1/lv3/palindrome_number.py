def num_to_str(num):
    if num >= 10:
        return chr(num + 65 - 10)
    else:
        return str(num)


def trans_to_b(num, b):
    result = ''
    while num >= b:
        tmp = num % b
        num = num // b
        result += num_to_str(tmp)
    result += num_to_str(num)
    return result[::-1]


def check_palindrome(transed):
    for i in range(len(transed)):
        if transed[i] != transed[-(i + 1)]:
            return False
    return True


def find_palindrome(b):
    result = []
    for i in range(1, 301):
        tmp = trans_to_b(i ** 2, b)
        if check_palindrome(tmp):
            result.append(i)
    return result


def main():
    testcase = 1
    while testcase != 0:
        testcase = int(input("2 ~ 30사이의 숫자를 입력하시오 [0: 정지] : "))
        if testcase == 0:
            break
        palindrome = find_palindrome(testcase)
        print(f"{len(palindrome)}개 ({palindrome}")
    return 0


main()
