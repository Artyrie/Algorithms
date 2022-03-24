# 1. set으로 단어 구성이 1개 차이나는 단어 검출
# 2. 1개 차이나면 변환


def solution(begin, target, words):
    # 80점, t1
    answer = 0
    n = len(begin)

    store = []
    while target in words:
        print("=====")
        print(f"words : {words}")
        print(f"store : {store}")
        candidate = []
        for word in words:
            tmp = len(set(begin).intersection(set(word)))
            if tmp == n - 1:
                candidate.append(word)
        print(f"candidate : {candidate}")
        if not candidate:
            begin = store[-1]
            store.pop()
        elif len(candidate) == 1:
            store.append(begin)
            begin = candidate[0]
            words.pop(words.index(candidate[0]))
        else:
            store.append(begin)
            if target in candidate:
                break
            tmp = []
            for i, word in enumerate(candidate):
                tmp.append((i, set(target).intersection(candidate[i])))
            tmp.sort(reverse=True, key=lambda x: len(x[1]))
            begin = candidate[tmp[0][0]]
            words.pop(words.index(candidate[tmp[0][0]]))


        print(f"begin : {begin}")

    print("end")
    print(begin, store)
    return len(store) if store else 0


def solution2(begin, target, words):
    # 100점, t5 max 14ms
    n = len(begin)

    store = []
    while target in words:
        candidate = []

        for word in words:
            diff = 0
            for b, w in zip(begin, word):
                if b != w:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                candidate.append(word)

        if not candidate:
            begin = store[-1]
            store.pop()
        elif len(candidate) == 1:
            store.append(begin)
            begin = candidate[0]
            words.pop(words.index(candidate[0]))
        else:
            store.append(begin)
            if target in candidate:
                break
            tmp = []
            for i, word in enumerate(candidate):
                tmp.append((i, set(target).intersection(candidate[i])))
            tmp.sort(reverse=True, key=lambda x: len(x[1]))
            begin = candidate[tmp[0][0]]
            words.pop(words.index(candidate[tmp[0][0]]))

    return len(store)


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])