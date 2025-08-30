# 재고 클래스

class Inventory:
    def __init__(self):
        self.items = {}
        
    def add_item(self, name, price, quantity):
        if name in self.items:
            (self.items[name])["quantity"] += quantity
            print(f"{name} 상품의 수량이 {(self.items[name])['quantity']}개로 변경되었습니다. ({quantity}개 추가)")
        else:    
            self.items[name] = {"price": price, "quantity": quantity}
            print(f"{name} 상품이 새로 추가되었습니다. 수량은 {quantity}개 입니다.")
        
    def sell_item(self, name, quantity_to_sell):
        if name not in self.items or quantity_to_sell > (self.items[name])["quantity"]:
            print("현재 판매가 불가능한 상품입니다.")
        else:
            (self.items[name])["quantity"] -= quantity_to_sell
            print(f"{name} 상품이 {quantity_to_sell}개 판매 완료 되었습니다. (현재 재고: {(self.items[name])['quantity']}개)")

    def get_stock_info(self):
        print("--- 재고 현황 ---")
        for i, k in self.items.items():
            print(f"상품: {i}, 가격: {k['price']}원, 수량: {k['quantity']}개")


# --- 실행 코드 ---
inventory = Inventory()

# 상품 입고
inventory.add_item("노트북", 1500000, 5)
inventory.add_item("마우스", 50000, 10)
inventory.add_item("노트북", 1500000, 3) # 재고 추가
print("-" * 20)

# 재고 현황 확인
inventory.get_stock_info()
print("-" * 20)

# 상품 판매
inventory.sell_item("마우스", 3) # 성공
inventory.sell_item("키보드", 1) # 없는 상품
inventory.sell_item("노트북", 10) # 재고 부족
print("-" * 20)

# 최종 재고 현황 확인
inventory.get_stock_info()

