class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}.")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_ability):
        super().__init__(name, age, coat_color)
        self.hunting_ability = hunting_ability

    def bark(self):
        print(f"{self.name} barks loudly!")

    def is_good_hunter(self):
        if self.hunting_ability >= 7:
            print(f"{self.name} is a good hunter.")
        else:
            print(f"{self.name} is not a very good hunter.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def snore(self):
        print(f"{self.name} snores loudly while sleeping.")

    def is_strong(self):
        if self.strength >= 8:
            print(f"{self.name} is very strong.")
        else:
            print(f"{self.name} is not exceptionally strong.")

dog1 = JackRussellTerrier("Tommy", 5, "White", 9)
dog2 = Bulldog("Brownie", 3, "Brown", 7)

dog1.description()
dog1.get_info()
dog1.bark()
dog1.is_good_hunter()

dog2.description()
dog2.get_info()
dog2.snore()
dog2.is_strong()
