import math


def read_testcase(name):
    f = open(f"c:/Users/Artyrie/Documents/algorithm/Algorithms book1/lv3/{name}", 'r')
    lines = f.readlines()
    tmp_line = []
    for line in lines:
        tmp_line.append(list(map(int, line.split())))
    f.close()
    return tmp_line


def make_number(n, p):
    total = 0
    for num in str(n):
        total += int(math.pow(int(num), p))
    return total


def main():
    tmp = read_testcase("input3.txt")

    for testcase in tmp[1:]:
        test = True
        num = testcase[0]
        pnum = testcase[1]
        dic = dict(num=1)
        while test:
            num = make_number(num, pnum)
            if num in dic:
                dic[num] += 1
                if dic[num] == 3:
                    test = False
            else:
                dic[num] = 1
        count = 0
        for val in dic.values():
            if val == 1:
                count += 1
        print(count)


main()