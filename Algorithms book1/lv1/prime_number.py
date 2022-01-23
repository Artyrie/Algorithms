def prime_number():
    count = 1
    print(1, end = ' ')

    for num in range(2, 1001):
        for i in range(1, num):
            if (i != 1 and num % i == 0):
                break
            elif (i == num - 1):
                count = count + 1
                if (count % 8 == 0):
                    print(num)
                else:
                    print(num, end = ' ')

    print(f"소수 개수 : {count}")

prime_number()