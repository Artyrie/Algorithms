import math
import numpy as np
from collections import Counter

def solution(answers):
    # 100점, t14, max 4.82ms
    t_answer = []
    answer = []
    n = len(answers)
    p1 = ([1, 2, 3, 4, 5] * math.ceil(n/5))[:n]
    p2 = ([2, 1, 2, 3, 2, 4, 2, 5] * math.ceil(n/8))[:n]
    p3 = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * math.ceil(n/10))[:n]
    for i, p in enumerate([p1, p2, p3], start=1):
        tmp = Counter(np.equal(answers, p))
        t_answer.append((tmp[True], i))

    t_answer.sort(key=lambda x: (-x[0], x[1]))

    for v, k in t_answer:
        if t_answer[0][0] == v:
            answer.append(k)
    return answer