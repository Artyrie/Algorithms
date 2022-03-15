def solution(numbers):
    # 폐기
    answer = ''
    index = [i for i in range(len(numbers))]

    for i in range(len(numbers)):
        tmp = -1
        max_val = answer + ''
        for _ in range(len(index)):
            j = index.pop(0)
            if answer + str(numbers[j]) > max_val:
                max_val = answer + str(numbers[j])
                if tmp != -1:
                    index.append(tmp)
                tmp = j
        answer = max_val + ''

    return answer


def solution2(numbers):
    # 33.3점, t5
    answer = ''
    numbers = sorted([str(v) for v in numbers],
                     reverse=True)

    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1] + '0':
            tmp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = tmp

    for val in numbers:
        answer += val

    return answer


def solution3(numbers):
    # 46.7점, t7
    answer = ''
    numbers = sorted([str(v) for v in numbers],
            key=lambda x: (-int(x[0]), len(x), -int(x)))

    while True:
        if len(numbers) > 1:
            tmp1 = numbers.pop(0)
            tmp2 = numbers.pop(0)
            tmp12 = (tmp1 + tmp2).ljust(6, "0")
            tmp21 = (tmp2 + tmp1).ljust(6, "0")
            if int(tmp12) > int(tmp21):
                answer += tmp1
                numbers.insert(0, tmp2)
            else:
                answer += tmp2
                numbers.insert(0, tmp1)
        else:
            answer += numbers.pop(0)
            break

    return answer


def solution4(numbers):
    # 33.3점, t5
    answer = ''
    numbers2 = sorted([str(num) for num in numbers],
                      reverse=True)


    for _ in range(len(numbers) - 1):
        n = len(answer)
        tmp_num = []
        for i in range(len(numbers2) - 1):
            if numbers2[i][0] != numbers2[i + 1][0]:
                tmp_num.append((answer + numbers2[i]).ljust(n + 4, "0"))
                break
            else:
                tmp_num.append((answer + numbers2[i]).ljust(n + 4, "0"))
                if i == len(numbers2) - 2:
                    tmp_num.append((answer + numbers2[i + 1]).ljust(n + 4, "0"))
        max_val = str(max(tmp_num))

        idx = []
        for i in range(len(tmp_num)):
            if tmp_num[i][0] != max_val[0]:
                break
            elif tmp_num[i] == max_val:
                idx.append(i)

        tmp_num = [numbers2[i] for i in idx]
        if len(tmp_num) == 1:
            answer += tmp_num[0]
            numbers2.remove(tmp_num[0])
        else:
            answer += min(tmp_num)
            numbers2.remove(min(tmp_num))

    answer += numbers2[0]

    return answer


def solution5(numbers):
    # 40점, t6
    answer = ''
    numbers = sorted([str(v) for v in numbers], reverse=True)

    digit_num = [[], [], [], []]
    for val in numbers:
        digit_num[len(val) - 1].append(val)

    while True:
        tmp = []
        for i in range(4):
            if digit_num[i] == []:
                tmp.append(-1)
            else:
                tmp.append(digit_num[i][0])
        n = len(answer)
        tmp = [(answer + t).ljust(n + 4, "0") if t != -1 else '0' for t in tmp]
        idx = tmp.index(max(tmp))
        answer += digit_num[idx].pop(0)

        if digit_num == [[], [], [], []]:
            break
        elif answer == '0':
            return '0'

    return answer


def solution6(numbers):
    # 100점, t15, 118.09ms
    answer = ''
    numbers = sorted([((str(num) * 4)[:4], str(num)) for num in numbers], reverse=True)

    if numbers[0][1] == '0':
        return '0'

    for val in numbers:
        answer += val[1]

    return answer


print(solution5([0, 0, 0, 0]))