def solution(prices):
    # 66.7점, t10, max 60.46ms
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        tmp = False
        for j in range(len(prices)):
            if i >= j:
                continue
            else:
                if tmp == False and prices[i] <= prices[j]:
                    answer[i] += 1
                elif tmp == False and prices[i] > prices[j]:
                    tmp = True
                    answer[i] += 1
                else:
                    continue

    return answer


def solution2(prices):
    # 66.7점, t10, max 30.13ms
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        val = prices[i]
        check = False
        for p1 in prices[i + 1:]:
            if val <= p1 and check == False:
                answer[i] += 1
                print("+")
            elif not check:
                check = True
                answer[i] += 1

    return answer


def solution3(prices):
    # 66.7점, t10, max 2.27ms
    answer = []
    for i in range(len(prices)):
        val = prices[i]
        ctr = 0
        for p in prices[i + 1:]:
            if val <= p:
                ctr += 1
            else:
                ctr += 1
                break
        answer.append(ctr)

    return answer


def solution4(prices):
    # 66.7점, t10, max 2.55ms
    answer = []
    curve = []
    for p1, p2 in zip(prices, prices[1:]):
        curve.append(p2 - p1)

    for i in range(len(prices)):
        tmp = 0
        ctr = 0
        for c in curve[i:]:
            tmp += c
            ctr += 1
            if tmp < 0:
                break
        answer.append(ctr)

    return answer


def solution5(prices):
    # 66.7점, t10, max 37.21ms
    p_len = len(prices)
    answer = [[0, 0] for _ in range(p_len)]

    for i in range(p_len - 1):
        for j in range(i + 1):
            if not answer[j][0] < 0:
                answer[j][0] += prices[i + 1] - prices[i]
                answer[j][1] += 1

    return [val[1] for val in answer]


def solution6(prices):
    # 100점, t10, max 1.02ms
    answer = []
    for i in range(len(prices)):
        ctr = 0
        for j in range(i + 1, len(prices)):
            ctr += 1
            if prices[i] > prices[j]:
                break
        answer.append(ctr)

    return answer