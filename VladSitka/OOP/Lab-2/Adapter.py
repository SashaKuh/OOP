
class Target:
    def request(self):
        return "Target: Default target's behavior."


class Adapter:
    def specific_request(self):
        return "Adaptee: Specific request."


class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        
        return self._adaptee.specific_request()


if __name__ == "__main__":
    adapter = Adapter()  
    adapter = Adapter(adapter)  

    
    print(adapter.request())  
