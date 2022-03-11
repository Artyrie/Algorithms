def solution1(participant, completion):
    # 90점 t5 5.38ms, 시간 초과
    part = set(participant)
    com = set(completion)
    tmp = list(part.difference(com))

    if tmp != []:
        answer = tmp[0]
    else:
        for com in completion:
            participant.remove(com)
        answer = participant[0]

    return answer


def solution2(participant, completion):
    # 70점
    def make_dic(tmp_list):
        tmp = {}
        for val in tmp_list:
            try:
                tmp[val] += 1
            except:
                tmp[val] = 1
        return sorted(tmp.items(), reverse=True,
                      key=lambda item: item[1])

    part = make_dic(participant)
    com = make_dic(completion)

    if len(part) != len(com):
        answer = set(participant).difference(set(completion))
        answer = list(answer)[0]
    else:
        answer = part[0][0]

    return answer


def solution3(participant, completion):
    # 100점 t5 0.52ms, 104.95ms
    if len(set(participant)) != len(set(completion)):
        answer = set(participant).difference(set(completion))
        return list(answer)[0]
    else:
        part = sorted(participant)
        com = sorted(completion)
        for p, c in zip(part, com):
            if p != c:
                return p
        return part[-1]
    return ''


def solution4(participant, completion):
    # 100점 t5 0.55ms, 102.25ms
    if len(set(participant)) != len(set(completion)):
        answer = set(participant).difference(set(completion))
        return list(answer)[0]
    else:
        part = sorted(participant)
        com = sorted(completion)
        for i in range(len(com)):
            if part[i] != com[i]:
                return part[i]
        return com[-1]
    return answer


def solution5(participant, completion):
    # 100점 t5 0.6ms, 77.92ms
    part = sorted(participant)
    com = sorted(completion)
    for p, c in zip(part, com):
        if p != c:
            return p
    return part[-1]


from collections import Counter


def solution6(participant, completion):
    # 100점 t5 0.66ms, 74.87ms
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]