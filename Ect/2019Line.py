import copy


# 8:16 ~
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


def cony_generate(cn_loc):
    tmp = []
    ctr = 0
    cony = cn_loc
    while cony + ctr <= CFG.MAX_LOC:
        cony += ctr
        ctr += 1
        tmp.append(cony)
    return tmp


def brown_next(br_loc, select, mode):
    if select == 1:
        return br_loc - 1 if mode else br_loc + 1
    elif select == 2:
        return br_loc + 1 if mode else br_loc - 1
    elif select == 3:
        return br_loc * 2 if mode else br_loc // 2


def find2x(cn_list, br_loc):
    ctr = 0
    tmp = copy.deepcopy(br_loc)
    while cn_list[ctr] > tmp:
        tmp = brown_next(tmp, 3, True)
        ctr += 1
    return ctr


"""
def check_cony(cn_list, br_loc, n):
    tmp = cn_list[n]
    for _ in range(n):
        if tmp % 2 > 0:
            tmp -= 1
        else:
            tmp = tmp // 2
    if tmp - br_loc != 0:
        return False
    else:
        return True
"""


def make_Nnext(br_loc):
    return [br_loc - 2, br_loc, 2 * (br_loc - 1), br_loc + 2, 2 * (br_loc + 1), 2 * (br_loc) - 1, 2 * (br_loc) + 1,
            4 * br_loc]


def make_select(process, ban_list):
    tmp = []
    for ban_process in ban_list:
        if len(ban_process) - len(process) == 1:
            if ban_process.startswith(process):
                tmp.append(int(ban_process[-1]))
        else:
            continue
    for i in range(3, 0, -1):
        if i in tmp:
            continue
        return i
    return 0


def solve(cn_list, br_loc, x2):
    """
    ctr = 0
    while ctr < x2 * 2:
        if check_cony(cn_list, br_loc, ctr):
            return ctr
        ctr += 1
    return -1
    """
    opt = CFG.MAX_LOC
    max_try = x2 * 2
    ctr = 0
    ban_list = []
    running = copy.deepcopy(br_loc)
    process = ''
    i = 0
    while ctr < max_try:
        if CFG.DEBUG:
            print(f"===== Debug {i} =====")
            i += 1
            print("process", process)
            print("ban", ban_list)
            print(len(ban_list))
            print(f"ctr : {ctr}, running : {running}, cony + 2: {cn_list[ctr + 2]}")
            print(f"opt : {opt}, max_try : {max_try}")
        if cn_list[ctr + 2] in make_Nnext(running):
            if opt > ctr + 2:
                opt = ctr + 2
            #print("check")
            ban_list.append(process)
            running = brown_next(running, int(process[-1]), False)
            process = process[:-1]
            ctr -= 1
        else:
            select = make_select(process, ban_list)
            if select < 1 or ctr + 2 >= opt:
                ban_list.append(process)
                if '' == ban_list[-1]:
                    return opt
                running = brown_next(running, int(process[-1]), False)
                process = process[:-1]
                ctr -= 1
            else:
                running = brown_next(running, select, True)
                process += str(select)
                ctr += 1
    if CFG.DEBUG:
        print("===== End =====")
        print("process", process)
        print("ban", ban_list)
        print(f"opt : {opt}, max_try : {max_try}")
    return -1


def main():
    testcase = read_testcase("2019line.txt")
    print(testcase)
    pos_cn = testcase[0]
    pos_br = testcase[1]

    cn_list = cony_generate(pos_cn)
    x2 = find2x(cn_list, pos_br)
    result = solve(cn_list, pos_br, x2)
    print(result)


main()
