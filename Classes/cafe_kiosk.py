# 카페 키오스크 클래스

class CafeKiosk:
    def __init__(self):
        self.menu = {}
        self.order = []

    def add_menu_item(self, item_name, price):
        self.menu[item_name] = price

    def display_menu(self):
        print(self.menu) 
    
    def add_to_order(self, item_name):
        if item_name in self.menu:
            self.order.append(item_name)
            print(f"{item_name} 메뉴를 주문에 추가했습니다.")
        else:
            print("메뉴에 없는 상품입니다.")
        
    def calculate_total(self):
        total_price = 0
        for i in self.order:
            total_price += self.menu[i]
        print(f"총 가격은 {total_price}원 입니다.")
    
    def clear_order(self):
        self.order.clear()
        print("주문이 초기화되었습니다.")


# --- 실행 코드 ---
kiosk = CafeKiosk()

# 메뉴 추가
kiosk.add_menu_item("아메리카노", 3000)
kiosk.add_menu_item("카페라떼", 4000)
kiosk.add_menu_item("카푸치노", 4000)

# 메뉴판 보여주기
kiosk.display_menu()
print("-" * 20)

# 주문
kiosk.add_to_order("아메리카노")
kiosk.add_to_order("카페라떼")
kiosk.add_to_order("에스프레소") # 없는 메뉴
print("-" * 20)

# 총액 계산
kiosk.calculate_total()
print("-" * 20)

# 주문 초기화
kiosk.clear_order()
kiosk.calculate_total() # 초기화 후 총액은 0원이어야 함
        
