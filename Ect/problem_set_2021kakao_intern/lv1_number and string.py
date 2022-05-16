def solution(s):
    # t10, max 0.04ms
    answer = ''
    num_dict = {"zero": 0, "one": 1, "two": 2, "three": 3,
                "four": 4, "five": 5, "six": 6, "seven": 7,
                "eight": 8, "nine": 9}
    tmp = ''
    for ns in s:
        if ns.isdigit():
            answer += ns
        else:
            tmp += ns
            try:
                tmp_num = num_dict[tmp]
                answer += str(tmp_num)
                tmp = ''
            except:
                continue

    return int(answer)