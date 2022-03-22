from collections import Counter


def solution1(number, k):
    # 25점, t3
    answer = ''
    t = 0
    while k > 0:
        tmp_val = ''.ljust(len(number), "0")
        tmp = 0

        for i in range(k + 1):
            if number[i:].ljust(len(number), "0") > tmp_val:
                tmp_val = number[i:].ljust(len(number), "0")
                tmp = i

        answer += number[tmp]
        number = number[tmp + 1:]
        k -= tmp
        t += 1

    answer += number

    return answer


def solution2(number, k):
    # 75점, t9
    answer = ''
    while k > 0:
        tmp = [0, 0]
        for i in range(k + 1):
            if tmp[0] < int(number[i]):
                tmp = [int(number[i]), i]

        k -= tmp[1]
        answer += number[tmp[1]]
        number = number[tmp[1] + 1:]

    answer += number

    return answer


def solution3(number, k):
    # 83.3점, t10
    answer = ''
    num = [int(s) for s in number]

    while k > 0:
        sort_num = sorted(num[:k + 1], reverse=True)
        idx = num.index(sort_num[0])
        answer += str(num[idx])
        num = num[idx + 1:]
        k -= idx

    return answer + ''.join(map(str, num))


def solution4(number, k):
    # 91.7점, t11
    answer = ''
    num = [int(s) for s in number]
    if len(set(num)) == 1:
        return number[k:]
    elif len(number) - 1 == k:
        return str(sorted(num, reverse=True)[0])

    while k > 0:
        sort_num = sorted(num[:k + 1], reverse=True)
        idx = num.index(sort_num[0])
        answer += str(num[idx])
        num = num[idx + 1:]
        k -= idx
        if len(num) == k:
            return answer

    return answer + ''.join(map(str, num))


def solution5(number, k):
    # 83.3점, t10
    num = [int(s) for s in number]
    if len(set(num)) == 1:
        return number[k:]
    elif len(number) - 1 == k:
        return str(sorted(num, reverse=True)[0])

    idx = 0
    while k > 0:
        for i in range(idx, len(num) - 1):
            if num[i] < num[i + 1]:
                num.pop(i)
                k -= 1
                idx = i - 1 if i - 1 > 0 else 0
                break
            elif i == len(num) - k:
                return ''.join(list(map(str, num[:len(number) - k])))

    return ''.join(list(map(str, num)))


def solution6(number, k):
    # 91.7점, t11
    answer = ''
    num = [int(s) for s in number]
    dict = Counter(num)
    dict = sorted(list(map(list, dict.items())), reverse=True)

    if len(dict) == 1:
        return number[k:]
    elif len(number) - 1 == k:
        return str(dict[0][0])

    while k > 0:
        for i in range(len(dict)):
            idx = num.index(dict[i][0])
            if idx <= k:
                dict[i][1] -= 1
                if dict[i][1] == 0:
                    dict.pop(i)
                break
            else:
                pass
        answer += str(num[idx])
        num = num[idx + 1:]
        k -= idx
        if len(num) == k:
            return answer

    return answer + ''.join(map(str, num))


def solution7(number, k):
    # 100점, t12, max 145.43ms
    stack = []
    for num in number:
        if stack == []:
            stack.append(num)
        elif stack[-1] < num:
            while stack != [] and k > 0:
                tmp = stack.pop()
                if tmp >= num:
                    stack.append(tmp)
                    break
                else:
                    k -= 1
            stack.append(num)
        elif len(number) - k > len(stack):
            stack.append(num)

    return ''.join(stack)