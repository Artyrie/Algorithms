def multiple_sum(num, max):
    multiple = [i for i in range(1, max + 1) if i % num == 0]
    return sum(multiple)

print(multiple_sum(4, 1000))