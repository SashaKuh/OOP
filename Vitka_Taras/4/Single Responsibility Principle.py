class TextGenerator:
    def generate_text(self):
        return "Hello, world!"

class TextPrinter:
    def print_text(self, text):
        print(text)

generator = TextGenerator()
printer = TextPrinter()

text = generator.generate_text()  
printer.print_text(text)          
