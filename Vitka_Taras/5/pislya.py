class InvoiceCalculator:
    def __init__(self, items, discount):
        self.items = items
        self.discount = discount

    def calculate_total(self):
        total = sum(self.items)
        total_after_discount = total - self.discount
        return total_after_discount

class InvoicePrinter:
    def print_invoice(self, items, discount, total):
        print("Invoice Details:")
        for item in items:
            print(f"Item: ${item}")
        print(f"Discount: ${discount}")
        print(f"Total: ${total}")
