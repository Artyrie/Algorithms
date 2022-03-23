from collections import Counter
import math


def solution1(people, limit):
    # 30점, t4, e2
    answer = 0
    info = sorted(map(list, Counter(people).items()), reverse=True)

    while len(info) > 0:
        stack = []
        print(info)
        while limit - sum(stack) > 40:
            print(stack)
            tmp = info.pop()
            if tmp[0] + sum(stack) > limit:
                info.append(tmp)
                break
            else:
                stack.append(tmp[0])
                if tmp[1] > 1:
                    info.append([tmp[0], tmp[1] - 1])
        print(stack)
        answer += 1

    return answer


def solution2(people, limit):
    # 75점, t15 max 11.56ms, e0
    answer = 0
    info = sorted(map(list, Counter(people).items()), reverse=True)

    while len(info) > 0:
        boat = info[-1][0]
        info[-1][1] -= 1
        if info[-1][1] < 1:
            info.pop()

        for i in range(len(info)):
            if info[i][0] + boat <= limit:
                info[i][1] -= 1
                if info[i][1] < 1:
                    info.pop(i)
                break

        answer += 1
    return answer


def solution3(people, limit):
    # 75점, t15 max 400.41ms, e0
    answer = 0
    people.sort(reverse=True)

    while len(people) > 0:
        boat = people.pop()

        for i in range(len(people)):
            if people[i] + boat <= limit:
                people.pop(i)
                break

        answer += 1
    return answer


def solution4(people, limit):
    # 65점, t10, e3
    answer = 0
    srt = sorted(people)

    while len(srt) > 0:
        boat = srt.pop(0)

        while srt != []:
            tmp = srt.pop()
            if boat + tmp <= limit:
                answer += 1
                break
            else:
                answer += 1
                if srt == []:
                    answer += 1

    return answer


def solution5(people, limit):
    # 100점, t15 max 0.82ms, e5 max 9.63ms
    answer = 0
    srt = sorted(people)
    lp = 0
    rp = len(srt) - 1

    while lp <= rp:
        if srt[lp] + srt[rp] <= limit:
            lp += 1
            rp -= 1
        else:
            rp -= 1
        answer += 1

    return answer