# Напишіть користувацький клас виключення з функціоналом на свій вибір.
# Викличте його за допомогую інструкції raise


class Storage:
    try:
        def __init__(self, product, quantity, brand):
            self.product = product
            self.quantity = quantity
            self.brand = brand
            if product == int or brand == int or quantity == str:
                raise Warning("incorrect input")
        def quantity_product(self):
            return f" product: {self.product} quantity: {self.quantity}"

        def quntity_brand(self):
            return f" under the brand: {self.brand} we have a product {self.product} and quntity {self.quantity}"
    except Exception as ex:
        return ex



trade_in_class = Storage("SSD", 120, "Samsung")
trade_in_class_2 = Storage("SSD", 80, "Kingston")
trade_in_class_3 = Storage("Notebbok", 12, "HP")

print(trade_in_class_2.quantity_product())

print(trade_in_class_2.quntity_brand())
print(trade_in_class.quantity_product())
print(trade_in_class.quntity_brand())
print(trade_in_class_3.quantity_product())
print(trade_in_class_3.quntity_brand())
