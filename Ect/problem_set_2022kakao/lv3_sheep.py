import copy
from collections import deque


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
    # 반례를 못 찾겠음
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

val = solution2([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
                [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9],
                 [10, 12], [12, 13], [13, 14]])
print("===== ======")
print(val)
