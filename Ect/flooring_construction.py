def flr_const(n):
    tmp = [1, 3]

    for i in range(2, n):
        val = tmp[i - 1] + 2 * tmp[i - 2]
        tmp.append(val)
    
    return tmp[n - 1] % 796796


print(flr_const(6))
