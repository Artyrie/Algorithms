from itertools import combinations


def manhatan_distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def find_reachable_p(room):
    tmp = []
    for r in range(5):
        for c in range(5):
            if room[r][c] == 'P':
                tmp.append((r, c))

    comb = list(combinations(tmp, 2))
    tmp = []
    for loc1, loc2 in comb:
        if manhatan_distance(loc1, loc2) <= 2:
            tmp.append((loc1, loc2))
    return tmp


def check_route(room, p_list):
    for loc1, loc2 in p_list:
        if manhatan_distance(loc1, loc2) < 2:  # 거리 1
            return False
        elif loc1[0] == loc2[0]:  # 행이 같은 거리 2
            if not room[loc1[0]][loc1[1] + 1] == 'X':
                return False
        elif loc1[1] == loc2[1]:  # 열이 같은 거리 2
            if not room[loc1[0] + 1][loc1[1]] == 'X':
                return False
        else:  # 일반 거리 2
            min_r = min(loc1[0], loc2[0])
            min_c = min(loc1[1], loc2[1])
            max_r = max(loc1[0], loc2[0])
            max_c = max(loc1[1], loc2[1])
            if loc1[1] > loc2[1]:  # 상승선 체크
                if not (room[min_r][min_c] == 'X' and
                        room[max_r][max_c] == 'X'):
                    return False
            else:  # 하락선 체크
                if not (room[min_r][max_c] == 'X' and
                        room[max_r][min_c] == 'X'):
                    return False
    return True


def solution(places):
    # t31, max 0.52ms
    answer = []

    while places:
        room = [list(p) for p in places.pop(0)]
        p_list = find_reachable_p(room)
        if check_route(room, p_list):
            answer.append(1)
        else:
            answer.append(0)
    return answer