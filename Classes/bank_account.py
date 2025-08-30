# 은행 계좌 클래스

class BankAccount:
    def __init__(self, owner_name, initial_deposit=0):
        self.owner_name = owner_name
        self.balance = 0
        self.transactions = []
        if initial_deposit > 0:
            self.balance += initial_deposit
            self.transactions.append(f"초기 입금: {initial_deposit} 원, 잔액: {self.balance} 원")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"입금: {amount} 원, 잔액: {self.balance} 원")
            print(f"입금: {amount} 원, 잔액: {self.balance} 원")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"출금: {amount} 원, 잔액: {self.balance} 원")
            print(f"출금: {amount} 원, 잔액: {self.balance} 원")
        elif amount <= 0:
            print(f"출금액이 잘못되었습니다.")
        else:
            print(f"잔액이 부족합니다.")

    def get_balance(self):
        print(f"계좌주: {self.owner_name}, 잔액: {self.balance} 원")

    def get_transaction_history(self):
        print("--- 거래 내역 ---")
        for i in self.transactions:
            print(i)

# --- 실행 코드 ---
account = BankAccount("드라간", 50000)
account.get_balance()
print("-" * 20)

# 입금 및 출금
account.deposit(20000)
account.withdraw(15000)
account.withdraw(60000) # 잔액 부족
print("-" * 20)

# 최종 잔액 및 거래 내역 확인
account.get_balance()
print("-" * 20)
account.get_transaction_history()
            