class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=5):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        subtotal = 0

        for product in self.products:
            subtotal += product.get_total()

        return subtotal

    def calculate_tax(self):
        subtotal = self.calculate_subtotal()
        return subtotal * self.tax_rate / 100

    def calculate_final_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        return subtotal + tax

    def display_bill(self):
        print("\n" + "=" * 55)
        print("                 FINAL BILL")
        print("=" * 55)

        print(f"{'Product':<20}{'Price':<10}{'Qty':<10}{'Total':<10}")
        print("-" * 55)

        for product in self.products:
            print(
                f"{product.name:<20}"
                f"₹{product.price:<9.2f}"
                f"{product.quantity:<10}"
                f"₹{product.get_total():.2f}"
            )

        print("-" * 55)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        final_total = self.calculate_final_total()

        print(f"{'Subtotal:':<40} ₹{subtotal:.2f}")
        print(f"{'Tax (' + str(self.tax_rate) + '%):':<40} ₹{tax:.2f}")
        print("=" * 55)
        print(f"{'Final Total:':<40} ₹{final_total:.2f}")
        print("=" * 55)


# Main Program

bill = Bill(tax_rate=5)

product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 500, 2)
product3 = Product("Keyboard", 1500, 1)

bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

bill.display_bill()