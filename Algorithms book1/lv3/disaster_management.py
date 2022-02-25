import copy


class CFG:
    MAX = 999


def read_testcase(name):
    tmp_case = []
    f = open(f"c:/Users/Artyrie/Documents/Algorithm/Algorithms book1/lv3/{name}", 'r')
    lines = f.readlines()

    for line in lines:
        tmp_line = list(map(str, line.split()))
        tmp_case.append(tmp_line)

    f.close()

    return tmp_case


def data_organization(file_name):
    testcase = read_testcase(file_name)
    meta_data = []

    for data in testcase[0]:
        meta_data.append(int(data))

    map = []
    for val in testcase[1:]:
        tmp = []
        for i in range(meta_data[1]):
            if (val[0][i] == 'E'):
                tmp.append(-1)
            elif (val[0][i] == 'F'):
                tmp.append(CFG.MAX)
            elif (val[0][i] == 'Y'):
                tmp.append(1)
            else:
                tmp.append(0)
        map.append(tmp)

    return meta_data, map


def print_map(map):
    for row in map:
        print(row)


def find_time_location(map, meta_data, time):
    horizon = meta_data[1]
    vertical = meta_data[0]
    time_pos = []
    for i in range(horizon):
        for j in range(vertical):
            if (map[i][j] == time):
                time_pos.append((i, j))
    return time_pos


def find_fire(map, meta_data):
    horizon = meta_data[1]
    vertical = meta_data[0]
    fire_pos = []
    for i in range(horizon):
        for j in range(vertical):
            if (map[i][j] == CFG.MAX):
                fire_pos.append((i, j))
    return fire_pos


def fire_spreading(map, meta_data):
    horizon = meta_data[1]
    vertical = meta_data[0]
    fire_pos = find_fire(map, meta_data)

    for pos_h, pos_v in fire_pos:
        if (pos_h - 1 > 0):
            map[pos_h - 1][pos_v] = CFG.MAX
        if (pos_v - 1 > 0):
            map[pos_h][pos_v - 1] = CFG.MAX
        if (pos_h + 1 < horizon):
            map[pos_h + 1][pos_v] = CFG.MAX
        if (pos_v + 1 < vertical):
            map[pos_h][pos_v + 1] = CFG.MAX


def check_near_safety(map, move_map, copy_map, meta_data, pos_h, pos_v, time):
    horizon = meta_data[1]
    vertical = meta_data[0]
    if (pos_h - 1 >= 0 and map[pos_h - 1][pos_v] < 0):
        map[pos_h - 1][pos_v] = time + 1
        copy_map[pos_h - 1][pos_v] = time + 1
        move_map[pos_h - 1][pos_v] = 'U'
        return True
    if (pos_v - 1 >= 0 and map[pos_h][pos_v - 1] < 0):
        map[pos_h - 1][pos_v] = time + 1
        copy_map[pos_h - 1][pos_v] = time + 1
        move_map[pos_h][pos_v - 1] = 'L'
        return True
    if (pos_h + 1 < horizon and map[pos_h + 1][pos_v] < 0):
        map[pos_h + 1][pos_v] = time + 1
        copy_map[pos_h + 1][pos_v] = time + 1
        move_map[pos_h + 1][pos_v] = 'D'
        return True
    if (pos_v + 1 < vertical and map[pos_h][pos_v + 1] < 0):
        map[pos_h][pos_v + 1] = time + 1
        copy_map[pos_h][pos_v + 1] = time + 1
        move_map[pos_h][pos_v + 1] = 'R'
        return True
    return False


def move(map, move_map, copy_map, meta_data, time):
    horizon = meta_data[1]
    vertical = meta_data[0]
    time_loc = find_time_location(map, meta_data, time)

    for pos_h, pos_v in time_loc:
        if (check_near_safety(map, move_map, copy_map, meta_data, pos_h, pos_v, time)):
            return True
        if (pos_h - 1 >= 0 and map[pos_h - 1][pos_v] == 0):
            map[pos_h - 1][pos_v] = time + 1
            move_map[pos_h - 1][pos_v] = 'U'
            copy_map[pos_h - 1][pos_v] = time + 1
        if (pos_v - 1 >= 0 and map[pos_h][pos_v - 1] == 0):
            map[pos_h][pos_v - 1] = time + 1
            move_map[pos_h][pos_v - 1] = 'L'
            copy_map[pos_h][pos_v - 1] = time + 1
        if (pos_h + 1 < horizon and map[pos_h + 1][pos_v] == 0):
            map[pos_h + 1][pos_v] = time + 1
            move_map[pos_h + 1][pos_v] = 'D'
            copy_map[pos_h + 1][pos_v] = time + 1
        if (pos_v + 1 < vertical and map[pos_h][pos_v + 1] == 0):
            map[pos_h][pos_v + 1] = time + 1
            move_map[pos_h][pos_v + 1] = 'R'
            copy_map[pos_h][pos_v + 1] = time + 1
    return False


def make_move_map(meta_data):
    horizon = meta_data[1]
    vertical = meta_data[0]
    move_map = [[0 for _ in range(horizon)] for _ in range(vertical)]
    return move_map


def next_route_pos(copy_map, meta_data, pos_h, pos_v, val):
    horizon = meta_data[1]
    vertical = meta_data[0]
    if (pos_h - 1 >= 0 and copy_map[pos_h - 1][pos_v] == val + 1):
        return (pos_h - 1, pos_v)
    elif (pos_v - 1 >= 0 and copy_map[pos_h][pos_v - 1] == val + 1):
        return (pos_h, pos_v - 1)
    elif (pos_h + 1 < horizon and copy_map[pos_h + 1][pos_v] == val + 1):
        return (pos_h + 1, pos_v)
    elif (pos_v + 1 < vertical and copy_map[pos_h][pos_v + 1] == val + 1):
        return (pos_h, pos_v + 1)


def make_route(map, move_map, copy_map, meta_data, spend_time):
    pos_h, pos_v = find_time_location(map, meta_data, 1)[0]
    val = 0

    while (True):
        if (val > 0):
            print(move_map[pos_h][pos_v], end="")
        val = copy_map[pos_h][pos_v]

        if (val > spend_time):
            break

        pos_h, pos_v = next_route_pos(copy_map, meta_data, pos_h, pos_v, val)

    return 0


def find_route(file_name):
    meta_data, map = data_organazation(file_name)
    fire_term = meta_data[2] + 1
    move_map = make_move_map(meta_data)
    copy_map = copy.deepcopy(map)
    spend_time = 0

    for time in range(1, CFG.MAX):
        if (time % fire_term == 0):
            fire_spreading(map, meta_data)
        if (move(map, move_map, copy_map, meta_data, time)):
            spend_time = time
            break

    print(spend_time)
    make_route(map, move_map, copy_map, meta_data, spend_time)

    return 0


find_route("input1.txt")
