from collections import Counter

def solution(citations):
    # 12.5점, t2
    h_index = Counter(sorted(citations))
    n = len(citations)
    answer = []
    acc = 0
    for k, v in h_index.items():
        if (n - acc) >= k and acc <= k:
            answer.append(k)
        acc += v

    return max(answer)


def solution(citations):
    # 100점, t16, max 4.93ms
    h_index = Counter(sorted(citations))
    n = len(citations)
    answer = []
    acc = 0
    for i in range(max(citations) + 1):
        try:
            val = h_index[i]
        except:
            val = 0
        if n - acc >= i >= acc:
            answer.append(i)
        acc += val

    return max(answer)