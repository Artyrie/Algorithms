def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)


def calculate(num):
    cnt = 0
    for i in range(num):
        for j in range(1, num + 1):
            if i > j:
                continue
            elif gcd(i, j) == 1:
                print(f"{i}/{j}")
                cnt += 1
    return cnt


def main():
    num = int(input("숫자 입력 : "))
    total = calculate(num)
    print(f"총 {total}개의 기약 분수가 존재")


main()
