import copy


class CFG():
    DEBUG = False
    MAX_LOC = 200000
    MIN_LOC = 0


def read_testcase(name):
    f = open(f"c:/Users/Artyrie/Documents/algorithm/Ect/{name}", 'r')
    line = f.readlines()
    tmp = list(map(int, line[0].split()))
    f.close()
    return tmp


def solve(pos_cn, pos_br):
    time = 0
    visit = [[False for i in range(CFG.MAX_LOC + 1)], [False for i in range(CFG.MAX_LOC + 1)]]
    queue = []
    pos_cur = copy.deepcopy(pos_br)
    queue.append(pos_cur)
    tmp = []

    while True:
        pos_cn += time
        visit[time % 2][pos_br] = True
        if CFG.DEBUG:
            print(f"===== {time} =====")
            print(visit[0][1:30])
            print(visit[1][1:30])

        if pos_cn > CFG.MAX_LOC:
            return -1
        if visit[time % 2][pos_cn]:
            return time

        for _ in range(len(queue)):
            val = queue[0]
            if val - 1 >= 0:
                visit[(time + 1) % 2][val - 1] = True
            queue.append(val - 1)
            visit[(time + 1) % 2][val + 1] = True
            queue.append(val + 1)
            visit[(time + 1) % 2][val * 2] = True
            queue.append(val * 2)
            tmp.append(val)
            queue.pop(0)

        time += 1


def main():
    testcase = read_testcase("2019line.txt")
    print(testcase)
    pos_cn = testcase[0]
    pos_br = testcase[1]

    result = solve(pos_cn, pos_br)
    print(result)


main()