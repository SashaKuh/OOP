# Приклад порушення принципу Single Responsibility
class BadEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_pay(self):
        # Розрахунок зарплати
        return self.salary * 0.85  # після податків
    
    def save_to_database(self):
        # Збереження в базу даних
        pass
    
    def generate_report(self):
        # Генерація звіту
        pass

# Правильна реалізація принципу Single Responsibility
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class PayrollCalculator:
    @staticmethod
    def calculate_pay(employee):
        # Клас відповідає тільки за розрахунок зарплати
        return employee.salary * 0.85

class EmployeeRepository:
    @staticmethod
    def save(employee):
        # Клас відповідає тільки за роботу з базою даних
        pass

class ReportGenerator:
    @staticmethod
    def generate_report(employee):
        # Клас відповідає тільки за генерацію звітів
        pass

# Приклад використання
if __name__ == "__main__":
    # Створюємо працівника
    employee = Employee("Іван Петренко", 10000)
    
    # Розраховуємо зарплату
    payroll = PayrollCalculator()
    net_salary = payroll.calculate_pay(employee)
    
    # Зберігаємо дані
    repository = EmployeeRepository()
    repository.save(employee)
    
    # Генеруємо звіт
    report = ReportGenerator()
    report.generate_report(employee)
