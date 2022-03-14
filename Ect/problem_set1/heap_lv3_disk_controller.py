import heapq as hq
import math


def solution(jobs):
    # 5점, t1
    hq.heapify(jobs)
    n = len(jobs)
    heap = []
    answer = 0
    time = 0

    while len(jobs) > 0:
        val = hq.heappop(jobs)
        hq.heappush(heap, [val[1], val[0]])

    while len(heap) > 0:
        val = hq.heappop(heap)
        time += val[0]
        answer += time - val[1]

    return answer / n


def solution2(jobs):
    # 20점, t4
    hq.heapify(jobs)
    n = len(jobs)
    heap = []
    answer = 0
    time = 0

    while True > 0:
        # 일을 다하면 종료
        if len(jobs) == 0 and len(heap) == 0:
            break

        # 현 시간에 가능한 일 추출
        while len(jobs) > 0:
            if jobs[0][0] <= time:
                val = hq.heappop(jobs)
                hq.heappush(heap, val[::-1])
            else:
                break

        # 일 수행
        if len(heap) > 0:
            val = hq.heappop(heap)
            time += val[0]
            answer += time - val[1]
        else:
            time += 1

    return answer / n


def solution3(jobs):
    # 100점, t20, 1.27ms
    # 문제 조건의 소수점 이하 버림을 확인하지않아 오답이였음
    hq.heapify(jobs)
    n = len(jobs)
    heap = []
    answer = 0
    time = 0

    while True > 0:
        # 일을 다하면 종료
        if len(jobs) == 0 and len(heap) == 0:
            break

        # 현 시간에 가능한 일 추출
        while len(jobs) > 0:
            if jobs[0][0] <= time:
                val = hq.heappop(jobs)
                hq.heappush(heap, val[::-1])
            else:
                break

        # 일 수행
        if len(heap) > 0:
            val = hq.heappop(heap)
            time += val[0]
            answer += time - val[1]
        else:
            time += 1

    return math.floor(answer / n)



# [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]] = 72
# [[0, 5], [2, 10], [10000, 2]] = 6