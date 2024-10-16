class Target:
    def request(self) -> str:
        return "Default Target: No specific implementation."


class Adaptee:
    def specific_request(self) -> str:
        return "Specific request from Adaptee."

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: {self.adaptee.specific_request()}"


if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    print(adapter.request())  
