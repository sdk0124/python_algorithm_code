from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛이 생성됨.")

    def damaged(self, damaged):
        self.hp -= damaged
        if (self.hp < 0):
            self.hp = 0            
        print(f"{self.name} 유닛이 {damaged}데미지를 입음. 남은 체력 : {self.hp}")
        if (self.hp <= 0):
            print(f"{self.name} 유닛 제거됨.")

    def move(self, location):
        print(f"{self.name} 유닛이 {location} 방향으로 이동. 속도 : {self.speed}")

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} 유닛이 {location} 방향 적군에게 {self.damage}만큼 공격.")
    
# 비행 유닛
class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, location):
        print(f"{self.name} 유닛이 {location} 방향으로 비행. 속도 : {self.flying_speed}")

# 비행 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(location)

# 비행 수송 유닛
class FlyableTransportUnit(Unit, Flyable):
    def __init__(self, name, hp, flying_speed):
        Unit.__init__(self, name, hp, 0)
        Flyable.__init__(self, flying_speed)
        self.board_list = []
    
    def board(self, unit):
        self.board_list.append = unit
        print(f"{self.name} 유닛에 {unit.name} 유닛이 탑승함.")

    def check_board_units(self):
        print("-- 현재 탑승 중인 유닛 --")
        for unit in self.board_list:
            print(f"{unit.name} 유닛")
    
    def get_off(self):
        for unit in self.board_list:
            print(f"{unit.name} 유닛 하강.")
            self.board_list.remove(unit)
        print(f"{self.name} 유닛이 비어있음.")

# ------------------------- #

class Marine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 40, 3, 5)
    
    def stimpack(self):
        if (self.hp > 10):
            self.hp -= 10
            print(f"{self.name} 유닛이 스팀팩 사용.")
        else:
            print(f"{self.name} 유닛이 체력이 부족하여 스팀팩 사용 취소.")

class Tank(AttackUnit):
    seize_developed = False
    def __init__(self):
        super().__init__("탱크", 150, 1, 30)
        self.seize_mode = False

    def set_seize_mode(self):
        if (Tank.seize_developed == False):
            return
        
        if (self.seize_mode == False):
            print(f"{self.name} 유닛이 시즈 모드 전환.")
            self.damage *= 2
            self.seize_mode = True
            self.speed = 0
        else:
            print(f"{self.name} 유닛이 시즈 모드 해제.")
            self.damage /= 2
            self.seize_mode = False
            self.speed = 1
        
class Wraith(FlyableAttackUnit):
    clocking_developed = False
    def __init__(self):
        super().__init__("레이스", 80, 10, 6)
        self.clocked = False
    
    def clocking(self):
        if (Wraith.clocking_developed == False):
            return
        
        if (self.clocked == False):
            self.clocked = True
            print(f"{self.name} 유닛이 클로킹 모드 전환.")            
        else:
            self.clocked = False
            print(f"{self.name} 유닛이 클로킹 모드 해제.")

def game_start():
    print("[게임 시작]")

def game_over():
    print("Player : gg")

game_start()
attack_units = []
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()
w2 = Wraith()

attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
attack_units.append(w2)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
Wraith.clocking_developed = True

for unit in attack_units:
    if (isinstance(unit, Marine)):
        unit.stimpack()
    if (isinstance(unit, Tank)):
        unit.set_seize_mode()
    if (isinstance(unit, Wraith)):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5, 20))

game_over()