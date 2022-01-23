import numpy as np

def number_find_game() : 
    answer = np.random.randint(100)
    print(answer)

    print("0부터 100까지의 숫자를 입력하세요")
    i = 1
    while(True) : 
        get_num = input(f"[{i}번째 도전] : ")
        get_num = int(get_num)

        if (answer > get_num) : 
            print(f"{get_num}보다 큽니다")
        elif (answer < get_num) : 
            print(f"{get_num}보다 작습니다")
        else : 
            print(f"정답입니다. {i}번째 만에 맞췄군요")
            break
        
        i += 1

number_find_game()