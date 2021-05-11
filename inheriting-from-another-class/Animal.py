class Animal:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"Animal name: {self.name} - size: {self.size}"


class Wolf(Animal):
    def __init__(self, name, size):
        super().__init__(name, size)

    def __repr__(self):
        return f"Wolf name: {self.name} - size: {self.size}"


class Bear(Animal):
    def __init__(self, name, size):
        super().__init__(name, size)

    def __repr__(self):
        return f"Bear name: {self.name} - size: {self.size}"


class Eagle(Animal):
    def __init__(self, name, size):
        super().__init__(name, size)

    def __repr__(self):
        return f"Eagle name: {self.name} - size: {self.size}"


class Duck(Animal):
    def __init__(self, name, size):
        super().__init__(name, size)

    def __repr__(self):
        return f"Duck name: {self.name} - size: {self.size}"


class Frog(Animal):
    def __init__(self, name, size, depth):
        super().__init__(name, size)
        self.depth = depth

    def __repr__(self):
        return f"Frog name: {self.name} - size: {self.size} - depth: {self.depth}"


class Trout(Animal):
    def __init__(self, name, size, depth):
        super().__init__(name, size)
        self.depth = depth

    def __repr__(self):
        return f"Trout name: {self.name} - size: {self.size} - depth: {self.depth}"


def main():
    wolf = Wolf("Lobito", "Medium")
    print(wolf)

    bear = Bear("Osito", "Large")
    print(bear)

    eagle = Eagle("Aguilita", "Small")
    print(eagle)

    duck = Duck("Patito", "Small")
    print(duck)

    frog = Frog("Sapito", "Small", 2)
    print(frog)

    trout = Trout("Pecesito", "Small", 25)
    print(trout)


if __name__ == '__main__':
    main()
