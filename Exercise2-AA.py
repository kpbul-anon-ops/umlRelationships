class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.__age)


person1 = Person("Lina", 20)
person1.display_info()