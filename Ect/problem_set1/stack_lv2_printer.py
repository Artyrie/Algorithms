def solution(priorities, location):
    # 100점, t20, max 0.70ms
    index = [i for i in range(len(priorities))]
    dic = {}
    ctr = 1

    while len(priorities) > 0:
        tmp = [priorities.pop(0), index.pop(0)]
        if priorities != [] and tmp[0] < max(priorities):
            priorities.append(tmp[0])
            index.append(tmp[1])
        else:
            dic[tmp[1]] = ctr
            ctr += 1

    return dic[location]


def solution2(priorities, location):
    # 100점, t20, max 4.52ms
    stack = [[p, -l] for p, l in zip(priorities, range(len(priorities)))]
    dic = {}
    ctr = 1

    while len(stack) > 0:
        tmp = stack.pop(0)
        if len(stack) != 0 and tmp[0] < max(map(max, stack)):
            stack.append(tmp)
        else:
            dic[-tmp[1]] = ctr
            ctr += 1

    return dic[location]


def solution3(priorities, location):
    # 100점, t20, max 0.5ms
    stack = [(idx, p) for idx, p in enumerate(priorities)]
    answer = 0

    while True:
        tmp = stack.pop(0)
        if any(tmp[1] < p[1] for p in stack):
            stack.append(tmp)
        else:
            answer += 1
            if tmp[0] == location:
                return answer


print(solution3([2, 1, 3, 2], 2))