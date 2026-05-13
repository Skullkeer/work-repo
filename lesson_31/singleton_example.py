class Player:
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def change_name(self, name):
        self.name = name

    def heal(self, hp):
        print(f"{self.name} heals for {hp}hp!")
        self.hp += hp

    def attack(self):
        print(f"{self.name} attacks with {self.weapon}!")

# Creational Design Pattern: Singleton
class PlayerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Note! Do not use __init__ in Singletons()
    # This will not work as intended without some guards.
    # Also, __new__ doubles as the getInstance() method in Python (if you are reading UML)

    def set_name(self, name):
        self.name = name

    def set_hp(self, hp):
        self.hp = hp

    def set_weapon(self, weapon):
        self.weapon = weapon

    # A bit redundant given we have set_name now!
    # We should remove this before the final version
    def change_name(self, name):
        self.name = name

    def heal(self, hp):
        print(f"{self.name} heals for {hp}hp!")
        self.hp += hp

    def attack(self):
        print(f"{self.name} attacks with {self.weapon}!")

# ====================

p1 = Player("Bob", 10, "Short sword")
p2 = Player("Bob", 10, "Short sword")

p1.heal(15)
p2.attack()

print("Player is not a Singleton")
print(f"p1 == p2: {p1 == p2} ")

p100 = Player("Fred", 1000, "Staff")

# Now, using the Singleton
print("")

p1 = PlayerSingleton()
p2 = PlayerSingleton()

p1.set_name("Nick")
p1.set_hp(200)
p1.set_weapon("Flail")

print("Player is a Singleton")
print(f"p1 == p2: {p1 == p2} ")

p1.attack()
p2.attack()
