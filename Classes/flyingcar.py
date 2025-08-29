# 플라잉카 클래스

class LandVehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        print("지상에서 주행 중입니다.")

class AerialVehicle:
    def __init__(self, altitude):
        self.altitude = altitude

    def fly(self):
        print("공중에서 비행 중입니다.")

class FlyingCar(LandVehicle, AerialVehicle):
    def __init__(self, name, speed, altitude):
        self.name = name
        LandVehicle.__init__(self, speed)
        AerialVehicle.__init__(self, altitude)

    def show_status(self):
        print(f"이름: {self.name}, 현재 속력: {self.speed}km/h, 현재 고도: {self.altitude}")

# --- 실행 코드 ---
my_car = FlyingCar("K-2025", 100, 500)

# 부모들에게 물려받은 메서드 사용
my_car.drive()
my_car.fly()

# 자식 클래스 고유의 메서드 사용
my_car.show_status()