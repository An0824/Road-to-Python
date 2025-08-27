# 게임캐릭터 클래스

class GameCharacter:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
    
    def attack(self, other_character):
        other_character.hp -= self.power
        print(f"{self.name}이(가) {other_character.name}에게 일반 공격을 가했습니다!")

    def show_status(self):
        print(f"{self.name}의 현재 체력: {self.hp}")


class Warrior(GameCharacter):
    def __init__(self, name, hp, power, defense):
        super().__init__(name, hp, power)
        self.defense = defense

    def power_slash(self, other_character):
        other_character.hp -= (self.power * 1.5)
        print(f"{self.name}이(가) {other_character.name}에게 파워 슬래시를 사용했습니다!")

class Mage(GameCharacter):
    def __init__(self, name, hp, power, mana):
        super().__init__(name, hp, power)
        self.mana = mana

    def fireball(self, other_character):
        other_character.hp -= (self.power * 2)
        print(f"{self.name}이(가) {other_character.name}에게 파이어볼을 사용했습니다!")




# --- 실행 코드 ---
warrior = Warrior("아서스", 100, 15, 5)
mage = Mage("제이나", 70, 20, 100)

warrior.show_status()
mage.show_status()
print("="*20)

# 전투 시작
warrior.attack(mage)
mage.fireball(warrior)

warrior.show_status()
mage.show_status()
print("="*20)

warrior.power_slash(mage)

warrior.show_status()
mage.show_status()