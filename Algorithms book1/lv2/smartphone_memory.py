class CFG():
    MAX = 100000

def read_testcase(name): 
    tmp_case = []
    f = open(f"c:/Users/Artyrie/Documents/Algorithm/Algorithms book1/lv2/{name}", 'r')
    lines = f.readlines()

    for line in lines: 
        tmp_line = list(map(int, line.split()))
        tmp_case.append(tmp_line)

    f.close()

    return tmp_case

def memory_table_init(memory, resource):
    memory_table = [CFG.MAX for _ in range(memory + 1)]
    memory_table[0] = 0
    for app_time, app_memory in resource:
        memory_table[app_memory] = app_time
    return memory_table

def is_full(memory, active_memory):
    if (memory - active_memory >= 0):
        return False
    else:
        return True

def memory(file_name):
    data = read_testcase(file_name)
    test_case_num = data[0][0]
    pos = 1
    result = []

    while(test_case_num > 0):
        # resource check
        memory = data[pos][1] - data[pos][0]
        app_num = data[pos + 1][0]
        app_resource = [data[pos + i] for i in range(2, app_num + 2)]
        pos += app_num + 2
        test_case_num -= 1

        # table init
        memory_table = memory_table_init(memory, app_resource)

        # table optimize
        for i in range(memory + 1):
            #print(memory_table)
            for app_time, app_memory in app_resource:
                #print(memory, i + app_memory)
                if (not(is_full(memory, i + app_memory))):
                    if (memory_table[i] + app_time < memory_table[i + app_memory]):
                        memory_table[i + app_memory] = memory_table[i] + app_time
                else:
                    if (memory_table[i] < CFG.MAX):
                        continue
                    else:
                        memory_table[i] = -1

        #print(memory_table[memory])
        result.append(memory_table[memory])

    return result

print(memory("input1.txt"))