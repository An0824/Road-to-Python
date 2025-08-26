# 스톱워치 클래스

import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.running = False
    
    def start(self):
        if self.running == True:
            print("스톱워치가 이미 실행 중입니다.")
        else:
            self.running = True
            self.start_time = time.time()
            print("스톱워치가 시작되었습니다.")

    def stop(self):
        if self.running == False:
            print("스톱워치가 시작되지 않았습니다.")
        else:
            self.running = False
            self.end_time = time.time()
            print("스톱워치가 멈췄습니다.")
        
    def reset(self):
        self.start_time = None
        self.end_time = None
        self.running = False
        print("스톱워치가 초기화되었습니다.")

    def get_elapsed_time(self):
        if self.running == True:
            time1 = time.time() - self.start_time
            print(f"경과 시간: {time1:.2f}초")
        elif self.start_time == None:
            print("측정 기록이 없습니다.")
        else:
            time2 = self.end_time - self.start_time
            print(f"최종 경과 시간: {time2:.2f}초")

# --- 실행 코드 ---
sw = Stopwatch()
sw.get_elapsed_time() # 시작 전

sw.start()
time.sleep(1) # 1초 대기
sw.get_elapsed_time() # 실행 중
time.sleep(1) # 1초 추가 대기
sw.stop()

sw.get_elapsed_time() # 멈춘 후
print("-" * 20)

sw.reset()
sw.get_elapsed_time() # 초기화 후

