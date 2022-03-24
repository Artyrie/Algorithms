def solution(tickets):
    # 50점, t2
    answer = ["ICN"]

    bad = []
    while tickets:
        dest = []
        for i, ticket in enumerate(tickets):
            if answer[-1] == ticket[0]:
                dest.append((i, ticket))

        dest.sort(key=lambda x: x[1][1])

        if not dest:
            tmp = answer.pop()
            bad.append(tmp)
        else:
            answer.append(dest[0][1][1])
            tickets.pop(dest[0][0])
            if bad:
                tickets.append(bad.pop())
    return answer


def solution2(tickets):
    # 100점, t4 max 0.05ms
    answer = [['ICN', 'ICN']]

    bad = []
    while tickets:

        dest = []
        for i, ticket in enumerate(tickets):
            if answer[-1][1] == ticket[0]:
                dest.append((i, ticket))

        dest.sort(key=lambda x: x[1][1])

        if not dest:
            tmp = answer.pop()
            bad.append(tmp)
        else:
            answer.append(dest[0][1])
            tickets.pop(dest[0][0])
            if bad:
                tickets.append(bad.pop())
    return [v for _, v in answer]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print("answer :", 	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print("\n\n\n")
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
print("answer :", ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])
print("\n\n\n")
print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]))
print("answer :", ["ICN", "SFO", "ICN", "SFO", "QRE"])