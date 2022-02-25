def read_testcase(name):
    f = open(f"c:/Users/Artyrie/Documents/algorithm/Algorithms book1/lv3/{name}", 'r')
    lines = f.readlines()
    tmp_line = list(map(int, lines))
    f.close()

    return tmp_line


def make_pocket(testcase, pn_index):
    pocket_num = testcase[pn_index]
    return testcase[pn_index + 1: pn_index + pocket_num + 1]


def mean_val(target):
    tmp = 0
    for val in target:
        tmp += val
    tmp /= len(target)
    return tmp


def solve(pocket):
    mean = mean_val(pocket)
    if mean.is_integer():
        mean = int(mean)
        cnt = 0
        for val in pocket:
            if val < mean:
                cnt += mean - val
        return cnt
    else:
        return -1


def main():
    testcase = read_testcase("input2.txt")
    test_num = 0
    pos = 1

    while test_num < testcase[0]:
        pocket = make_pocket(testcase, pos)
        result = solve(pocket)
        print(result)
        pos += testcase[pos] + 1
        test_num += 1


main()