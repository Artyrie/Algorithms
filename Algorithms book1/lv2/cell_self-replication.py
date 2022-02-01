def read_testcase(name): 
    tmp_case = []
    f = open(f"c:/Users/Artyrie/Documents/Algorithm/Algorithms book1/lv2/{name}", 'r')
    lines = f.readlines()

    for line in lines: 
        tmp_line = list(map(int, line.split()))
        tmp_case.append(tmp_line)

    f.close()

    return tmp_case

def data_extraction(file_name):
    data = read_testcase(file_name)
    test_case_num = data[0][0]
    pos = 1
    result = []

    while(test_case_num > 0):
        dna_num = data[pos][0]
        dna_pattern = data[pos + 1]
        result.append((dna_num, dna_pattern))
        test_case_num -= 1
        pos += 2
    
    return result

def cell_debug(dna_num, dna_pattern):
    dna_1st = 0
    dna_last = dna_num - 1
    tmp = [0 for _ in range(dna_num)]

    for i in range(dna_num):
        if (tmp[i] == 0):
            if (i == dna_1st):
                if (dna_pattern[i + 1] != 0):
                    tmp[i] = dna_pattern[i]
                elif (dna_pattern[i] != 0):
                    tmp[i + 1] = dna_pattern[i]
            elif (i == dna_last):
                if (dna_pattern[i] != tmp[i - 1]):
                    print("Error")
                    return [-1 for _ in range(dna_num)]
            else:
                if (dna_pattern[i] != 0):
                    test_val = dna_pattern[i] - tmp[i - 1]
                    if (test_val == dna_pattern[i] and
                        dna_pattern[i + 2] == 0):
                        pass
                    else:
                        tmp[i + 1] = dna_pattern[i] - tmp[i - 1]
                else:
                    if (dna_pattern[i - 1] != 0):
                        pass        

    if (tmp == [0 for _ in range(dna_num)]):
        print("end")
        return dna_pattern
    return tmp


def cell_calculation(file_name):
    data = data_extraction(file_name)
    
    for dna_num, dna_pattern in data:
        test = dna_pattern
        divide = 0
        while(not(-1 in test)):
            divide += 1
            tmp = cell_debug(dna_num, test)
            print(tmp)
            if (tmp == test):
                break
            else:
                test = tmp

        print("================")
        print(f"{divide - 1}회 분할")

cell_calculation("input2.txt")