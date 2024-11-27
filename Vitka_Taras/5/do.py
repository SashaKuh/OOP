class Invoice:
    def __init__(self, items, discount):
        self.items = items
        self.discount = discount

    def calculate_total(self):
        total = sum(self.items)
        total_after_discount = total - self.discount
        return total_after_discount

    def print_invoice(self):
        total = self.calculate_total()
        print("Invoice Details:")
        for item in self.items:
            print(f"Item: ${item}")
        print(f"Discount: ${self.discount}")
        print(f"Total: ${total}")
