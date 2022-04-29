import copy
from collections import deque
from itertools import combinations


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

    print(sheep)
    path_dict = {s: find_route(0, s, edges) for s in sheep}
    print(path_dict)

    visited = []
    cnt = 0
    while True:
        print("======")
        print(f"sheep : {sheep}")
        print(f"visited : {visited}")
        print(f"answer : {answer}")

        dest = sheep.popleft()
        print("dest:", dest)
        # 가야 할 경로 파악
        route = []
        for p in path_dict[dest]:
            if p not in visited:
                route.append(p)
        print(route)

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

    print(sheep)
    path_dict = {s: find_route(0, s, edges) for s in sheep}
    print(path_dict)
    visited = []
    check = 0
    while check >= 0:
        print("======")
        print(f"dict : {path_dict}")
        print(f"visited : {visited}")
        print(f"answer : {answer}")

        dest_list = sheep_efn(sheep, visited, path_dict)
        print(dest_list)

        for dest in dest_list:
            print("------ ------")
            print("dest:", dest)
            # 가야 할 경로 파악
            route = []
            for p in path_dict[dest[0]]:
                if p not in visited:
                    route.append(p)
            print(f"route : {route}")
            reachable, ratio = cal_sheep(route, info, answer)
            print(f"reachable : {reachable}")
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

    print(sheep)
    path_dict = {s: find_route(0, s, edges) for s in sheep}
    print(path_dict)
    visited = []
    check = 0
    while check >= 0:
        print("======")
        print(f"dict : {path_dict}")
        print(f"visited : {visited}")
        print(f"answer : {answer}")

        dest_list = sorted(sheep_efn2(sheep, visited, path_dict).items(), reverse=True)
        print(f"dest_list : {dest_list}")

        # 우선 순위 파악
        for _, dest in dest_list:
            check2 = 0
            print("------ ------")
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
            print("dest:", dest)

            # 가야 할 경로 파악
            for d in dest:
                route = []
                for p in path_dict[d]:
                    if p not in visited:
                        route.append(p)
                print(f"route : {route}")
                reachable, ratio = cal_sheep(route, info, answer)
                print(f"reachable : {reachable}")
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

    print(sheep)
    path_dict = {s: find_route(0, s, edges) for s in sheep}
    print(path_dict)

    # 노드 사용 빈도
    tmp_dict = {}
    for key, val in path_dict.items():
        for v in val:
            try:
                tmp_dict[v] += 1
            except:
                tmp_dict[v] = 1
    print(tmp_dict)
    # 루트 공통 사용률
    efn_dict = {s: 0 for s in sheep}
    for key in sheep:
        for v in path_dict[key]:
            efn_dict[key] += tmp_dict[v]
    print(efn_dict)

    visited = []
    check = 0
    while check >= 0:
        print("======")
        print(f"dict : {path_dict}")
        print(f"visited : {visited}")
        print(f"answer : {answer}")

        dest_list = sorted(sheep_efn2(sheep, visited, path_dict).items(), reverse=True)
        print(f"dest_list : {dest_list}")

        # 우선 순위 파악
        for _, dest in dest_list:
            check2 = 0
            print("------ ------")
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
            print("dest:", dest)

            # 가야 할 경로 파악
            for d in dest:
                route = []
                for p in path_dict[d]:
                    if p not in visited:
                        route.append(p)
                print(f"route : {route}")
                reachable, ratio = cal_sheep(route, info, answer)
                print(f"reachable : {reachable}")
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


val = solution4([0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
                [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [6, 9],
                 [7, 10], [9, 11], [10, 12], [11, 13]])
print("===== ======")
print(val)
