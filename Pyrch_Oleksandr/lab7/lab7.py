class Гра:
    def __init__(self, назва, геймплей):
        self.назва = назва
        self.геймплей = int(геймплей)
        
    def визначення_назви(self):
        return self.назва
    
    def цікавий_геймплей(self):
        if self.геймплей >= 7:
            return "Супер"
        else:
            return "Погано"

моя_гра = Гра("Little Nighmares II", "9")
print(моя_гра.визначення_назви())
print(моя_гра.цікавий_геймплей())
print("__________________________________________")

class Студія(Гра):
    def __init__(self, назва):
        self.назва = назва
    
    def назва_студії(self):
        return self.назва
    
студії = Студія("Tarsier Studios")
print(студії.назва_студії())