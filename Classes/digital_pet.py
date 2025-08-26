# 디지털펫 클래스

class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger_level = 50 # 배고픔 수치, 초기값 50

    def speak(self):
        if self.animal_type == "강아지":
            print("멍멍!")
        elif self.animal_type == "고양이":
            print("야옹~")
        else:
            print(f"{self.name}이(가) 울음소리를 냅니다.")

    def feed(self):
        self.hunger_level -= 15
        if self.hunger_level < 0: 
            self.hunger_level = 0 # 배고픔 수치는 음수가 될 수 없음
        print(f"{self.name}의 배고픔 수치가 {self.hunger_level}이/가 되었습니다.")
        

    def check_status(self):
        print(f"이름: {self.name}, 종류: {self.animal_type}, 배고픔: {self.hunger_level}")