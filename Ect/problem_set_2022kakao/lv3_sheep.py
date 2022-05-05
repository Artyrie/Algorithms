import copy
import numpy as np
from collections import deque
from itertools import combinations
from itertools import permutations


def find_route(src, dest, edges):
    result = [dest]

    while dest != src:
        for edge in edges:
            if dest == edge[1]:
                result.append((edge[0]))
                dest = edge[0]
    result.reverse()
    return result


def cal_sheep(target, info, ratio):
    result = copy.deepcopy(ratio)
    reachable = True
    for i in target:
        if info[i]:
            result[1] += 1
        else:
            result[0] += 1
        if result[0] <= result[1]:
            reachable = False
    return reachable, result  # [양, 늑대]


def solution1(info, edges):
    # t11, 61.1점 오답 2 7 9 10 12 14 16
    answer = [0, 0]  # 양, 늑대
    sheep = deque([])

    for i, val in zip(range(len(info)), info):
        if val == 0:
            sheep.append(i)

    path_dict = {s: find_route(0, s, edges) for s in sheep}

    visited = []
    cnt = 0
    while True:
        dest = sheep.popleft()
        # 가야 할 경로 파악
        route = []
        for p in path_dict[dest]:
            if p not in visited:
                route.append(p)

        reachable, ratio = cal_sheep(route, info, answer)
        if reachable:
            answer = ratio
            visited.extend(route)
            cnt = 0
        else:
            sheep.append(dest)
            cnt += 1

        if cnt == len(sheep):
            break

    return answer[0]


def sheep_efn(sheep, visited, path):
    result = []
    for key, val in path.items():
        get_wolves = 1
        get_sheep = 0
        for v in val:
            if v not in visited:
                if v in sheep:
                    get_sheep += 1
                else:
                    get_wolves += 1
        result.append((key, round(get_sheep / get_wolves, 2)))
    return sorted(result, key=lambda x: -x[1])


def solution2(info, edges):
    # t16, 88.9점 오답 12 16
    answer = [0, 0]  # 양, 늑대
    sheep = deque([])

    for i, val in zip(range(len(info)), info):
        if val == 0:
            sheep.append(i)

    path_dict = {s: find_route(0, s, edges) for s in sheep}

    visited = []
    check = 0
    while check >= 0:
        dest_list = sheep_efn(sheep, visited, path_dict)

        for dest in dest_list:
            # 가야 할 경로 파악
            route = []
            for p in path_dict[dest[0]]:
                if p not in visited:
                    route.append(p)

            reachable, ratio = cal_sheep(route, info, answer)
            if reachable:
                answer = ratio
                if not route:
                    visited.append(0)
                else:
                    visited.extend(route)
                    for r in route:
                        if r in sheep:
                            path_dict.pop(r)
                check = 1
                break
        if check == 0:
            break
        else:
            check = 0

    return answer[0]


def sheep_efn2(sheep, visited, path):
    result = {}
    for key, val in path.items():
        get_wolves = 1
        get_sheep = 0
        for v in val:
            if v not in visited:
                if v in sheep:
                    get_sheep += 1
                else:
                    get_wolves += 1
        tmp = round(get_sheep / get_wolves, 2)
        try:
            result[tmp].append(key)
        except:
            result[tmp] = [key]
    return result


def solution3(info, edges):
    # t17, 94.4점 오답 16
    answer = [0, 0]  # 양, 늑대
    sheep = deque([])

    for i, val in zip(range(len(info)), info):
        if val == 0:
            sheep.append(i)

    path_dict = {s: find_route(0, s, edges) for s in sheep}
    visited = []
    check = 0
    while check >= 0:
        dest_list = sorted(sheep_efn2(sheep, visited, path_dict).items(), reverse=True)

        # 우선 순위 파악
        for _, dest in dest_list:
            check2 = 0
            # 같은 효율이 여러 개면, 공통된 루트가 많은 것을 찾음
            if len(dest) > 1:
                combination = list(combinations(dest, 2))
                tmp_efn = []
                for comb in combination:
                    tmp_val = set(path_dict[comb[0]]).intersection(path_dict[comb[1]])
                    tmp_efn.append((len(tmp_val), comb))
                tmp_efn = sorted(tmp_efn, reverse=True)
                tmp = []
                for _, tmp_val in tmp_efn:
                    tmp.extend(list(tmp_val))
                    if set(tmp) == set(dest):
                        dest = tmp
                        break

            # 가야 할 경로 파악
            for d in dest:
                route = []
                for p in path_dict[d]:
                    if p not in visited:
                        route.append(p)

                reachable, ratio = cal_sheep(route, info, answer)
                if reachable:
                    answer = ratio
                    if not route:
                        visited.append(0)
                    else:
                        visited.extend(route)
                        for r in route:
                            if r in sheep:
                                path_dict.pop(r)
                    check = 1
                    check2 = 1
                    break
            if check2 == 1:
                break
        if check == 0:
            break
        else:
            check = 0

    return answer[0]


def get_not_visited_sheep(visited, sheep):
    result = []
    for s in sheep:
        if s not in visited:
            result.append(s)
    return result


def solution4(info, edges):
    # t17, 94.4점 오답 16. 16 반례를 못 찾은 개선
    answer = [0, 0]  # 양, 늑대
    sheep = deque([])

    for i, val in zip(range(len(info)), info):
        if val == 0:
            sheep.append(i)

    path_dict = {s: find_route(0, s, edges) for s in sheep}

    # 노드 사용 빈도
    tmp_dict = {}
    for key, val in path_dict.items():
        for v in val:
            try:
                tmp_dict[v] += 1
            except:
                tmp_dict[v] = 1

    # 루트 공통 사용률
    efn_dict = {s: 0 for s in sheep}
    for key in sheep:
        for v in path_dict[key]:
            efn_dict[key] += tmp_dict[v]

    visited = []
    check = 0
    while check >= 0:
        dest_list = sorted(sheep_efn2(sheep, visited, path_dict).items(), reverse=True)

        # 우선 순위 파악
        for _, dest in dest_list:
            check2 = 0
            # 같은 효율이 여러 개면, 공통된 루트가 많은 것을 찾음
            if len(dest) > 1:
                combination = list(combinations(get_not_visited_sheep(visited, sheep), 2))
                tmp_efn = []
                for comb in combination:
                    tmp_val = set(path_dict[comb[0]]).intersection(path_dict[comb[1]])
                    tmp_efn.append((len(tmp_val), comb))
                tmp_efn = sorted(tmp_efn, reverse=True)
                tmp_dict = {d: 0 for d in dest}
                for val, (k1, k2) in tmp_efn:
                    if k1 in dest:
                        tmp_dict[k1] += val
                    if k2 in dest:
                        tmp_dict[k2] += val
                tmp = []
                for key, val in sorted(tmp_dict.items(), key=lambda x: -x[1]):
                    tmp.append(key)
                    if set(tmp) == set(dest):
                        dest = tmp
                        break

            # 가야 할 경로 파악
            for d in dest:
                route = []
                for p in path_dict[d]:
                    if p not in visited:
                        route.append(p)

                reachable, ratio = cal_sheep(route, info, answer)
                if reachable:
                    answer = ratio
                    if not route:
                        visited.append(0)
                    else:
                        visited.extend(route)
                        for r in route:
                            if r in sheep:
                                path_dict.pop(r)
                    check = 1
                    check2 = 1
                    break
            if check2 == 1:
                break
        if check == 0:
            break
        else:
            check = 0

    return answer[0]


def solution5(info, edges):
    # t18, max 2768.86ms
    sheep = []  # 양 위치 기록
    for i, val in zip(range(len(info)), info):
        if val == 0:
            sheep.append(i)

    path_dict = {s: find_route(0, s, edges) for s in sheep}  # 양으로 가는 경로 파악

    sheep_only = []  # 양만 있는 경우
    for key, val in path_dict.items():
        if not set(val) - set(sheep):
            sheep_only.append(key)

    # 늑대를 포함한 양 경로 순열
    left = list(set(sheep) - set(sheep_only))
    perm_list = list(permutations(left, len(left)))

    max_score = len(sheep_only)
    while perm_list:
        perm = perm_list.pop()
        visited = copy.deepcopy(sheep_only)
        sheep_count = np.array([len(sheep_only), 0])
        # 순열에 따라 방문
        for p in perm:
            route = path_dict[p]
            tmp_count = copy.deepcopy(sheep_count)
            reachable = tmp_count[0] - tmp_count[1]
            # 루트 체크
            for r in route:
                print(reachable)
                if r in visited:
                    continue
                else:
                    visited.append(r)
                    if info[r] == 0:
                        tmp_count[0] += 1
                        reachable += 1
                    else:
                        tmp_count[1] += 1
                        reachable -= 1
                    if reachable < 1:
                        break

            # 경로 도달 가능성 확인
            if reachable < 1:
                break
            else:
                sheep_count = tmp_count
        # 최고 점수 갱신 확인
        if max_score < sheep_count[0]:
            max_score = int(sheep_count[0])
    return max_score
