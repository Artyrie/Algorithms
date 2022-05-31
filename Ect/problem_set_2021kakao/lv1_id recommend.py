import re


def solution(new_id):
    answer = ''
    regex = re.compile(r'[0-9A-Za-z-_\.]')
    tmp_id = regex.findall(new_id)

    tmp_str = ''
    for idx, s in zip(range(len(tmp_id)), tmp_id):
        if idx == 0 and s == '.': # 4조건
            tmp_str = s
            continue
        if tmp_str == '.' and s == '.': # 3조건
            continue
        answer += s.lower() # 1조건
        tmp_str = s

    if len(answer) == 0: # 5조건
        answer += 'a'
    else: # 6조건
        answer = answer[:15]

    if answer[-1] == '.': # 4조건
        answer = answer[:-1]

    if len(answer) < 3:
        for i in range(3 - len(answer)):
            answer += answer[-1]
    return answer


def solution2(new_id):
    tmp_id = new_id
    tmp_id = tmp_id.lower()
    tmp_id = re.sub('[^a-z0-9\-_\.]', '', tmp_id)
    tmp_id = re.sub('\.+', '.', tmp_id)
    tmp_id = re.sub('^\.|\.$', '', tmp_id)
    tmp_id = 'a' if tmp_id == '' else tmp_id[:15]
    tmp_id = re.sub('^\.|\.$', '', tmp_id)

    if len(tmp_id) < 3:
        for _ in range(3 - len(tmp_id)):
            tmp_id += tmp_id[-1]
    return tmp_id