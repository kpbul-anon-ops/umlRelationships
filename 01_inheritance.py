# Inheritance (Is-a): Dog IS-A Animal
class Animal:
    def __init__(self, name: str):
        self.name = name


# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"


if __name__ == "__main__":
    # 1. Instantiate a Dog; name is handled by the Animal parent
    my_dog = Dog("Buddy")

    # 2. Use the inherited attribute and the subclass method
    print(my_dog.name)
    print(my_dog.bark())
