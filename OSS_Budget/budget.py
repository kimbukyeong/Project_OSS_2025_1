import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


    def __init__(self):
        self.imports=[]

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Imports(today, category, description, amount)
        self.imports.append(imports)
        print("수입이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.imports:
            print("수입 내역이 없습니다.\n")
            return
        print("\n[수입 목록]")
        for idx, e in enumerate(self.imports, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.imports)
        print(f"총 수입: {total}원\n")
