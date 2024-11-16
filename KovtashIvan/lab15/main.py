"""
# Брудний код (закоментований для прикладу)
class calc:
    def do_stuff(self,n1,n2,op):
        if op=='+':
            r=n1+n2
        elif op=='-':
            r=n1-n2
        elif op=='*':
            r=n1*n2
        elif op=='/':
            if n2!=0:
                r=n1/n2
            else:
                r="Помилка"
        return r

    def show(self,n1,n2,op,r):
        print(f"{n1} {op} {n2} = {r}")

# Використання брудного коду
c=calc()
num1=10
num2=5
for op in ['+','-','*','/']:
    res=c.do_stuff(num1,num2,op)
    c.show(num1,num2,op,res)
"""

# Чистий код після рефакторингу
class Calculator:
    
    @staticmethod
    def add(x: float, y: float) -> float:
        return x + y
    
    @staticmethod
    def subtract(x: float, y: float) -> float:
        return x - y
    
    @staticmethod
    def multiply(x: float, y: float) -> float:
        return x * y
    
    @staticmethod
    def divide(x: float, y: float) -> float | str:
        if y != 0:
            return x / y
        return "Помилка: ділення на нуль"

class CalculatorDisplay:    
    @staticmethod
    def show_result(x: float, y: float, operation: str, result: float | str):
        print(f"{x} {operation} {y} = {result}")

if __name__ == "__main__":
    calculator = Calculator()
    display = CalculatorDisplay()
    
    # Тестові числа
    x, y = 10, 5
    
    result = calculator.add(x, y)
    display.show_result(x, y, '+', result)
    
    result = calculator.subtract(x, y)
    display.show_result(x, y, '-', result)

    result = calculator.multiply(x, y)
    display.show_result(x, y, '*', result)
    
    result = calculator.divide(x, y)
    display.show_result(x, y, '/', result)
    
    result = calculator.divide(x, 0)
    display.show_result(x, 0, '/', result)
