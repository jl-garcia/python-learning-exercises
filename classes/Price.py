class Price:
    def __init__(self, part_number, price):
        self.part_number = part_number
        self.price = price

    def get_price(self):
        return self.price


# 2.
def function__init__(self, part_number, price):
    self.part_number = part_number
    self.price = price


def function_get_price(self):
    return self.price


#
def set_discount(self, percent_off):
    self.percent_off = percent_off


def get_discount_price(self):
    return self.price - self.price * (self.percent_off / 100)


def main():
    # 1.
    price1 = Price(1, 22.2)
    print(price1.get_price())

    # 3.
    name_space = dict(__init__=function__init__, get_price=function_get_price)

    # 4.
    Price2 = type('Price2', (), name_space)

    # 5.
    demo = Price2(2, 33.3)
    print(demo.get_price())

    # Milestone 2
    item_price = Price("AAA_XD", 50.40)

    # Attributes in instance
    print(dir(item_price))
    print(item_price.__dict__)

    print("----------")
    # Attributes in class
    print(dir(Price))
    print(Price.__dict__)

    print("----------")
    # Add new functions to an existing object
    item_price.set_discount = set_discount
    item_price.get_discount_price = get_discount_price
    item_price.set_discount(item_price, 50)
    print(f"item_price {item_price.get_discount_price(item_price)}")

    # Add new functions to an existing class
    Price.set_discount = set_discount
    Price.get_discount_price = get_discount_price
    price_with_discount = Price("demo", 150)
    price_with_discount.set_discount(10)
    print(f"price_with_discount: {price_with_discount.get_discount_price()}")


if __name__ == "__main__":
    main()
