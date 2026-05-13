from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, name):
        pass

class StrategyStudyMath(Strategy):
    def execute(self, name):
        print(f"{name} is now doing math")

class StrategyStudyIT(Strategy):
    def execute(self, name):
        print(f"{name} is now doing it")

class StrategyStudyEnglish(Strategy):
    def execute(self, name):
        print(f"{name} is now doing english")

class Student:
    def __init__(self, name, study_strategy):
        self.name = name
        self.study_strategy = study_strategy

    def study(self):
        self.study_strategy.study()

    def set_strategy(self, new_strat):
        self.study_strategy = new_strat

# =============================

s = Student("Jade", StrategyStudyMath)
s.study
