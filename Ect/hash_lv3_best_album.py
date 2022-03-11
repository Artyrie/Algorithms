def solution(genres, plays):
    # 20점 t3
    table = []
    dic = {}

    for i, genre, play in zip(range(len(genres)), genres, plays):
        table.append((i, genre, play))
        try:
            dic[genre] += play
        except:
            dic[genre] = play

    priority = sorted(dic.keys(), reverse=True,
                      key=lambda x: x[1])
    priority_dic = {}

    ctr = 0
    for genre in priority:
        priority_dic[genre] = ctr
        ctr += 1

    sorted_table = sorted(table,
                          key=lambda x: (priority_dic[x[1]], -x[2], x[0]))

    answer = []
    ctr = 0
    tmp = sorted_table[0][1]
    for i, genre, _ in sorted_table:
        if ctr < 2 and tmp == genre:
            ctr += 1
            answer.append(i)
        elif ctr > 0 and tmp != genre:
            ctr = 1
            answer.append(i)
            tmp = genre
        else:
            continue

    return answer


def solution2(genres, plays):
    # 100점 t15
    table = []
    dic = {}

    for i, genre, play in zip(range(len(genres)), genres, plays):
        table.append((i, genre, play))
        try:
            dic[genre] += play
        except:
            dic[genre] = play

    priority = sorted(dic.items(), reverse=True,
                      key=lambda x: x[1])
    priority_dic = {}

    ctr = 0
    for genre, _ in priority:
        priority_dic[genre] = ctr
        ctr += 1

    sorted_table = sorted(table,
                          key=lambda x: (priority_dic[x[1]], -x[2], x[0]))

    answer = []
    ctr = 0
    tmp = sorted_table[0][1]
    for i, genre, _ in sorted_table:
        if ctr < 2 and tmp == genre:
            ctr += 1
            answer.append(i)
        elif ctr > 0 and tmp != genre:
            ctr = 1
            answer.append(i)
            tmp = genre
    return answer


def solution3(genres, plays):
    answer = []
    dic = {genre: [] for genre in set(genres)}

    for idx, genre, play in zip(range(len(genres)), genres, plays):
        dic[genre].append((idx, play))

    priority = sorted(list(dic.keys()), reverse=True,
                      key=lambda g: sum(list(map(lambda x: x[1], dic[g]))))

    for genre in priority:
        val_list = sorted(dic[genre],
                          key=lambda x: (-x[1], x[0]))
        val_list = [idx for idx, play in val_list]
        answer += val_list[:min(2, len(val_list))]

    return answer