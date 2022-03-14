import heapq


def solution(scoville, K):
    # 81점, t12, max 0.67ms
    heapq.heapify(scoville)

    answer = 0
    while scoville[0] < K:
        val1 = heapq.heappop(scoville)
        val2 = heapq.heappop(scoville)
        heapq.heappush(scoville, val1 + val2 * 2)
        answer += 1

    return answer


def solution2(scoville, K):
    # 100점, t16, max 0.66ms
    heapq.heapify(scoville)

    answer = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        val1 = heapq.heappop(scoville)
        val2 = heapq.heappop(scoville)
        heapq.heappush(scoville, val1 + val2 * 2)
        answer += 1

    return answer