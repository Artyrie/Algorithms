import copy

class CFG:
    MAX = 1000
    BLOCK = 1

def read_testcase(name): 
    tmp_case = []
    f = open(f"c:/Users/Artyrie/Documents/Algorithm/Algorithms book1/lv1/{name}", 'r')
    lines = f.readlines()

    for line in lines: 
        tmp_line = list(map(int, line.split()))
        tmp_case.append(tmp_line)

    f.close()

    return tmp_case

def print_map(map):
    for line in map:
        print(line)
    return 0

def make_block(block_size):
    block_list = []
    for i in range(1, block_size + 1):
        for j in range(1, block_size + 1):
            if (i <= j):
                block_list.append((i, j))
    return block_list

def near_checking(map, pos, val):
    map_xsize = len(map)
    map_ysize = len(map[0])
    x, y = pos
    pos_list = []
    if (x + 1 < map_xsize and map[x + 1][y] == val):
        pos_list.append(((x, y), (x + 1, y)))
    if (x - 1 >= 0 and map[x - 1][y] == val):
        pos_list.append(((x - 1, y), (x, y)))
    elif (y + 1 < map_ysize and map[x][y + 1] == val):
        pos_list.append(((x, y), (x, y + 1)))
    elif (y - 1 >= 0 and map[x][y - 1] == val):
        pos_list.append(((x, y - 1), (x, y)))
    return pos_list

def masonry_location(map, block):
    x, y = block
    test = set([])
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (map[i][j] == x):
                tmp = near_checking(map, (i, j), y)
                test = test | set(tmp)
    return list(test)

def remove_ban_list(location_list, ban_list):
    for test_set in location_list:
        for ban in ban_list:
            if (ban in test_set):
                test_set.remove(ban)
            
    return 0

def make_location_list(map, block_list, ban_list):
    location_list = []
    for x, y in block_list:
        test = masonry_location(map, (x, y))
        location_list.append(test)
    
    remove_ban_list(location_list, ban_list)
    return sorted(location_list, key = lambda x : len(x))

def must_dup(must_list):
    length = len(must_list)
    tmp = set()
    for line in must_list:
        for pos in line:
            tmp = tmp | set(pos)
    if (len(list(tmp)) != 2 * length):
        return True
    return False


def must_masonry(map, block_list, must_list):
    used_list = []

    for pos in must_list:
        pos1, pos2 = list(pos)[0]
        x1, y1 = pos1
        x2, y2 = pos2
        block_list.remove((min(map[x1][y1], map[x2][y2]), max(map[x1][y1], map[x2][y2])))
        #tmp = block_list.pop((map[x1][y1], map[x2][y2]))
        used_list.append((map[x1][y1], map[x2][y2]))
        map[x1][y1] = CFG.MAX + CFG.BLOCK
        map[x2][y2] = CFG.MAX + CFG.BLOCK
        CFG.BLOCK = CFG.BLOCK + 1
    return used_list

def choice_masonry(map, block_list, block):
    pos1, pos2 = block
    x1, y1 = pos1
    x2, y2 = pos2
    block_list.remove((min(map[x1][y1], map[x2][y2]), max(map[x1][y1], map[x2][y2])))
    map[x1][y1] = CFG.MAX + CFG.BLOCK
    map[x2][y2] = CFG.MAX + CFG.BLOCK
    CFG.BLOCK = CFG.BLOCK + 1
    return 0

def masonry(map, block_list):
    must_loc = make_location_list(map, block_list, [])
    must_list = [val for val in must_loc if len(val) == 1]
    must_masonry(map, block_list, must_list)

    copy_map = copy.deepcopy(map)
    copy_block_list = copy.deepcopy(block_list)

    print("========== Start =======")

    ban_list = []
    choice_list = []
    tc = 0
    while(len(copy_block_list) > 0):
        print(f"============ {tc} test line ==========")
        print_map(copy_map)
        location_list = make_location_list(copy_map, copy_block_list, ban_list)
        must_list = [val for val in location_list if len(val) == 1]
        if ([] in location_list or must_dup(must_list)):
            print(" ========= reset ========== ")
            copy_map = copy.deepcopy(map)
            copy_block_list = copy.deepcopy(block_list)
            ban_list.append(choice_list[-1])
            choice_list = []
            CFG.BLOCK = 3
            tc += 1
            continue

        if (len(must_list) != 0):
            must_masonry(copy_map, copy_block_list, must_list)
            continue

        choice_masonry(copy_map, copy_block_list, location_list[0][0])
        choice_list.append(location_list[0][0])

    return copy_map

def main():
    data = read_testcase("input1.txt")
    block_size = data[0][0]
    map = data[1:]
    block_list = make_block(block_size)
    
    map = masonry(map, block_list)
    print("======= result =======")
    print_map(map)

main()