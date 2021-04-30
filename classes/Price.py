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


if __name__ == "__main__":
    main()
