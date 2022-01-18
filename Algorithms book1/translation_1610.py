import re

class Translator : 
    def __init__(self) : 
        self.mode = 0
        self.number = 0

    def check_mode(self, mode) : 
        if (mode in ("A", "a", "B", "b")) : 
            return True
        else : 
            return False
    
    def get_mode(self) : 
        return self.mode

    def set_mode(self) : 
        while(True) : 
            print("10진수 <-> 16진수 변환 프로그램")
            print("10진수 -> 16진수 : A 입력")
            print("16진수 -> 10진수 : B 입력")
            mode = input("입력하세요 : ")

            if(self.check_mode(mode) == True) : 
                break
        
        self.mode = mode.lower()
        return True

    def check_num(self, num) : 
        if (self.mode == 'a') :
            p = re.compile('\d*\D\d*')
        else :
            p = re.compile('\w*\W\w*')
        m = p.match(num)

        if m : 
            return False
        else : 
            return True

    def get_num(self) : 
        return self.number

    def set_num(self) : 
        while(True) : 
            number = input("변환할 숫자를 입력하세요 : ")

            if(self.check_num(number) == True) : 
                break

        self.number = number
        return True

    def translate(self) : 
        self.set_mode()
        self.set_num()

        if (self.mode == 'a') : 
            print(f"10진수 값 : {self.number} -> 16진수 값 : {hex(int(self.number))}")
            return True
        else : 
            print(f"16진수 값 : {self.number} -> 10진수 값 : {int(self.number, 16)}")
            return True

ts = Translator()
ts.translate()