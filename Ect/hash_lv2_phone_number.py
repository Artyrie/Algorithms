from collections import Counter


def solution(phone_book):
    # 91.7 t20 2811.21ms
    phone = sorted(phone_book)
    for val in phone:
        for val2 in phone:
            tmp = hash(val)
            if tmp == hash(val2):
                continue
            if tmp == hash(val2[:len(val)]):
                return False
    return True


def solution2(phone_book):
    # 91.7점 t18
    min_len = sorted(phone_book, key=lambda val: len(val))
    min_len = len(min_len[0])
    phone = [val[:min_len] for val in phone_book]
    dict = sorted(Counter(phone).items(),
                  reverse=True, key=lambda x: x[1])
    if dict[0][1] > 1:
        return False
    return True


def solution3(phone_book):
    # 91.7점 t20 1211.05ms
    phone = sorted(phone_book, key=lambda val: len(val))
    for val in phone:
        val_len = len(val)
        tmp = [t[:val_len] for t in phone]
        dic = Counter(tmp)
        if dic[val] > 1:
            return False
    return True


def solution4(phone_book):
    # 91.7점 t20 902.13ms
    for val1 in phone_book:
        for val2 in phone_book:
            if val1 != val2 and val1.startswith(val2):
                return False
    return True


def solution5(phone_book):
    # 91.7점 t20 587.97ms
    phone = sorted(phone_book)
    for val1 in phone:
        for val2 in phone:
            if val1[0] < val2[0]:
                break
            elif val1[0] > val2[0]:
                continue
            else:
                if val1 != val2 and val1.startswith(val2):
                    return False
    return True


def solution6(phone_book):
    # 91.7점 t20 89.25ms
    phone = sorted(phone_book)
    for i in range(len(phone)):
        for j in range(i + 1, len(phone)):
            if phone[i][0] != phone[j][0]:
                break
            else:
                if phone[j].startswith(phone[i]):
                    return False
    return True

def solution7(phone_book):
    # 91.7점 t18 5.63ms
    tmp = sorted(phone_book, key=lambda val: len(val))
    min_len = len(tmp[0])
    max_len = len(tmp[-1])
    for i in range(min_len, max_len):
        tmp = [val[:i] for val in phone_book]
        tmp = sorted(Counter(tmp).items(), reverse=True,
                    key=lambda x: x[1])
        if tmp[0][1] > 1:
            return False
    return True


def solution8(phone_book):
    # 100점 t20 3.45ms
    tmp = sorted(phone_book, key=lambda val: len(val))
    min_len = len(tmp[0])
    max_len = len(tmp[-1])
    for i in range(min_len, max_len):
        tmp = [val[:i] for val in phone_book]
        tmp = sorted(Counter(tmp).items(), reverse=True,
                    key=lambda x: x[1])
        if tmp[0][1] > 1 and tmp[0][0] in phone_book:
            return False
    return True


def solution9(phone_book):
    # 100점 t20 1.07ms
    phone = sorted(phone_book)
    for c, v in zip(phone, phone[1:]):
        if v.startswith(c):
            return False
    return True