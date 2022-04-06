def solution(id_list, report, k):
    # t24, max 207.34ms
    report = set(report)
    # 유저 : 신고한 id, 유저가 신고당한 횟수, 나를 신고한 id
    dic = {idv: [[], 0, []] for idv in id_list}
    res = {idv: 0 for idv in id_list}

    for st in report:
        tmp = st.split(' ')
        idv = tmp[0]
        reported = tmp[1]
        dic[idv][0].append(reported)
        dic[reported][1] += 1
        dic[reported][2].append(idv)

    for idv in id_list:
        if dic[idv][1] >= k:
            for val in dic[idv][2]:
                res[val] += 1

    return list(res.values())