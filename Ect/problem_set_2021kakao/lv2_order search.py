import bisect


def solution(info, query):
    # t18 max 211.32ms, e0
    answer = []
    info = sorted([p.split() for p in info],
                  key=lambda x: -int(x[-1]))
    for i in range(len(query)):
        qry = ' '.join(query[i].split(' and ')).split()
        cnt = 0
        for person in info:
            check = True
            if int(person[-1]) < int(qry[-1]):
                break
            for p, q in zip(person[:-1], qry[:-1]):
                if q == '-':
                    continue
                elif p != q:
                    check = False
                    break
            if check:
                cnt += 1
        answer.append(cnt)
    return answer


def solution2(info, query):
    # t18 max 48.15ms, e0
    answer = []
    dic = {}
    info = [p.split() for p in info]
    for ti in info:
        for t0 in ['-', ti[0]]:
            for t1 in ['-', ti[1]]:
                for t2 in ['-', ti[2]]:
                    for t3 in ['-', ti[3]]:
                        try:
                            dic[t0 + t1 + t2 + t3].append(int(ti[4]))
                        except:
                            dic[t0 + t1 + t2 + t3] = [int(ti[4])]

    for i in range(len(query)):
        qry = ' '.join(query[i].split(' and ')).split()
        score = int(qry[-1])
        qry = ''.join(qry[:-1])
        try:
            answer.append(len(list(filter(lambda x: x>= score, dic[qry]))))
        except:
            answer.append(0)
    return answer


def solution3(info, query):
    # t18 max 46.15ms, e4 max 750.91ms
    answer = []
    dic = {}
    info = [p.split() for p in info]
    for ti in info:
        for t0 in ['-', ti[0]]:
            for t1 in ['-', ti[1]]:
                for t2 in ['-', ti[2]]:
                    for t3 in ['-', ti[3]]:
                        try:
                            dic[t0 + t1 + t2 + t3].append(int(ti[4]))
                        except:
                            dic[t0 + t1 + t2 + t3] = [int(ti[4])]
    for k in dic.keys():
        dic[k].sort()
    for i in range(len(query)):
        qry = ' '.join(query[i].split(' and ')).split()
        score = int(qry[-1])
        qry = ''.join(qry[:-1])
        try:
            answer.append(len(dic[qry]) - bisect.bisect_left(dic[qry], score))
        except:
            answer.append(0)
    return answer


solution3(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])