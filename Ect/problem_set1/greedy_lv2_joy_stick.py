def solution(name):
    # 22.2점, t6
    answer = 0
    val_A = ord("A")
    val_Z = ord("Z")

    ctr_A = 0
    for i in range(len(name)):
        if name[i] == 'A':
            ctr_A += 1
            continue
        tmp = ord(name[i])
        answer += min(tmp - val_A, val_Z - tmp + 1)
    answer += len(name) - ctr_A - 1
    return answer


def solution2(name):
    # 33.3점, t9
    answer = 0
    val_A = ord("A")
    val_Z = ord("Z")

    list_A = []
    ctr_A = 0
    for i in range(len(name)):
        if name[i] == 'A':
            ctr_A += 1
            continue
        else:
            list_A.append(ctr_A)
            ctr_A = 0
        tmp = ord(name[i])
        answer += min(tmp - val_A, val_Z - tmp + 1)

    answer += len(name) - max(list_A) - 1
    return answer


def solution3(name):
    # 44.4점, t12
    if set(name) == {'A'}:
        return 0

    answer = 0
    val_A = ord("A")
    val_Z = ord("Z")

    list_A = []
    ctr_A = 0
    for i in range(len(name)):
        if name[i] == 'A':
            ctr_A += 1
            continue
        else:
            list_A.append(ctr_A)
            ctr_A = 0
        tmp = ord(name[i])
        answer += min(tmp - val_A, val_Z - tmp + 1)
    list_A.pop(0)

    if max(list_A) == 0:
        return answer + len(name) -1
    elif len(list_A) == 1:
        return answer + len(name) - 1 - list_A[0]
    else:
        max_val = len(name) - 1
        for i in range(len(list_A)):
            l_A = list_A[:i]
            r_A = list_A[i + 1:]
            t1 = (sum(l_A) + len(l_A)) * 2 + sum(r_A) + len(r_A) + 1
            t2 = (sum(r_A) + len(r_A) + 1) * 2 + sum(l_A) + len(l_A)
            if min(t1, t2) < max_val:
                max_val = min(t1, t2)
        return answer + max_val


def solution4(name):
    # 100점, t27, max 0.03ms
    if set(name) == {'A'}:
        return 0

    answer = 0
    val_A = ord("A")
    val_Z = ord("Z")

    dist = []
    last_val = ''
    for i in range(len(name)):
        if last_val == name[i]:
            dist[-1][1] += 1
        else:
            dist.append([name[i], 1])
            last_val = name[i]
        answer += min(ord(name[i]) - val_A,
                      val_Z - ord(name[i]) + 1)

    min_val = len(name) - 1
    for i in range(len(dist)):
        if not dist[i][0] == 'A':
            continue
        ld = [v for k, v in dist[:i]]
        rd = [v for k, v in dist[i + 1:]]
        if ld == []:
            t1 = sum(rd)
        else:
            t1 = (sum(ld) - 1) * 2 + sum(rd)
        if rd == []:
            t2 = sum(ld) - 1
        else:
            t2 = sum(rd) * 2 + sum(ld) - 1
        if min(t1, t2) < min_val:
            min_val = min(t1, t2)

    return answer + min_val