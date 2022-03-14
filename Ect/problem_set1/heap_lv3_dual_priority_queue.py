import heapq as hq


def solution(operations):
    # 100점, t6, 0.04ms
    number = []

    for e in operations:
        tmp = e.split()
        operation = tmp[0]
        num = int(tmp[1])

        if operation == 'D':
            if num == 1 and len(number) > 0:
                number.remove(max(number))
            elif num == -1 and len(number) > 0:
                number.remove(min(number))
        elif operation == 'I':
            number.append(num)

    if len(number) == 0:
        return [0, 0]
    else:
        return [max(number), min(number)]


def solution2(operations):
    #100점, t6, 0.05ms
    min_heap = []
    max_heap = []

    for e in operations:
        tmp = e.split()
        operation = tmp[0]
        num = int(tmp[1])

        if operation == 'D':
            if num == 1 and len(max_heap) > 0:
                hq.heappop(max_heap)
                min_heap = [-v for v in max_heap]
                hq.heapify(min_heap)
            elif num == -1 and len(min_heap) > 0:
                hq.heappop(min_heap)
                max_heap = [-v for v in min_heap]
                hq.heapify(max_heap)
        elif operation == 'I':
            hq.heappush(max_heap, -num)
            hq.heappush(min_heap, num)

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [-hq.heappop(max_heap), hq.heappop(min_heap)]