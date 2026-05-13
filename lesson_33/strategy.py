from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, name):
        pass

class StrategyAgro(Strategy):
    def execute(self, name):
        print(f"{name} is agro")

class StrategyPatrol(Strategy):
    def execute(self, name):
        print(f"{name} is patrol")

class StrategySleep(Strategy):
    def execute(self, name):
        print(f"{name} is sleeping")

class Enemy:
    def __init__(self, name, hp, strategy):
        self.name = name
        self.hp = hp
        self.strategy = strategy

    def act(self):
        self.strategy.execute(self.name)

# =============================

enemies = []
e1 = Enemy("robot", 10, StrategyPatrol())
e2 = Enemy("goblin", 5, StrategySleep())
e3 = Enemy("Berserker", 5, StrategyAgro())

enemies.append(e1)
enemies.append(e2)
enemies.append(e3)

for enemy in enemies:
    enemy.act()
