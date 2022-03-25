def solution(triangle):
    # 100점, t10 max 2.65ms, e10 62.02ms
    answer = [[] for _ in range(len(triangle))]
    answer[0].append(triangle[0][0])

    cnt = 1
    for i in range(len(triangle) - 1):

        for j in range(cnt + 1):
            if j == 0:
                answer[i + 1].append(answer[i][j] + triangle[i + 1][j])
            elif j == cnt:
                answer[i + 1].append(answer[i][j - 1] + triangle[i + 1][j])
            else:
                answer[i + 1].append(max(answer[i][j - 1] + triangle[i + 1][j], answer[i][j] + triangle[i + 1][j]))

        cnt += 1
    return max(answer[-1])