class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description

    def __str__(self):
        return f'Expense({self.category}, {self.amount}, {self.description})'

class Income:
    def __init__(self, source, amount):
        self.source = source
        self.amount = amount

    def __str__(self):
        return f'Income({self.source}, {self.amount})'

class Budget:
    def __init__(self):
        self.expenses = []
        self.incomes = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def total_income(self):
        return sum(income.amount for income in self.incomes)

    def balance(self):
        return self.total_income() - self.total_expenses()

class User:
    def __init__(self, name):
        self.name = name
        self.budget = Budget()

    def __str__(self):
        return f'User({self.name})'

class FinanceTracker:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.name] = user

    def get_user(self, name):
        return self.users.get(name)

    def show_balance(self, user_name):
        user = self.get_user(user_name)
        if user:
            return f'{user.name} Balance: {user.budget.balance()}'
        return 'User not found'

# Пример использования
tracker = FinanceTracker()

# Создаем пользователя
user1 = User("Alice")
tracker.add_user(user1)

# Добавляем доходы и расходы
user1.budget.add_income(Income("Salary", 3000))
user1.budget.add_income(Income("Freelance", 500))
user1.budget.add_expense(Expense("Rent", 1200, "Monthly rent"))
user1.budget.add_expense(Expense("Groceries", 300, "Weekly groceries"))

# Выводим общий баланс
print(tracker.show_balance("Alice"))  