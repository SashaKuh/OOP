class Rectangle():
    def __init__(self,weight,height):
        self.weiht=int(weight)
        self.height=int(height)
    def __str__(self):
        return f"Площа даного чотирикутника: {self.area}"
    def area(self):
        return int(2*(self.weight+self.height))
c=Rectangle(4,5)
print(c)
