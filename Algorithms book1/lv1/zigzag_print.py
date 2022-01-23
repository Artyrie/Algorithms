def zigzag_print(per_line, max_num):
    count = 1
    odd = True

    for i in range(1, max_num + 1):
        if (odd):
            if (count == per_line):
                odd = not(odd)
                count = 0
                print(i)
            else:
                print(i, end = ' ')
        else:
            if (count == per_line):
                odd = not(odd)
                count = 0
                print(i - count - per_line + 1)
            else:
                print(i + (per_line - count * 2) + 1, end = ' ')

        count += 1

zigzag_print(3, 12)