import math

def solution(progresses, speeds):
    # 100점 t11
    answer = []
    days = []
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
    ctr = 0
    tmp = days[0]

    for val in days:
        if tmp < val:
            tmp = val
            answer.append(ctr)
            ctr = 1
        else:
            ctr += 1

    answer.append(ctr)
    return answer


def solution(progresses, speeds):
    # 100점 t11
    days = []
    for p, s in zip(progresses, speeds):
        tmp = math.ceil((100 - p) / s)
        if len(days) == 0 or days[-1][0] < tmp:
            days.append([tmp, 1])
        else:
            days[-1][1] += 1

    return [day[1] for day in days]

