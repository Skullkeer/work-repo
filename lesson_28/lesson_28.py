# Has-a relationship: composition
#
# is-a relationship: inheritance

class Engine:
    def __init__(self, num_cylinders, displacement, aspiration):
        self.num_cylinders = num_cylinders
        self.displacement = displacement
        self.aspiration = aspiration

    def turn_on(self):
        print("engine turns on")

    def turn_off(self):
        print("engine turns off")

class Car:
    def __init__(self, engine, brand, model):
        self.engine = engine
        self.brand = brand
        self.model = model

    def turn_on(self):
        self.engine.turn_on()
        print("The car turns on")

    def turn_off(self):
        self.engine.turn_off()
        print("the car turns off")





engine = Engine(4, 1800, "natural")
car = Car(engine, "toyata", "corolla")

car.turn_on()
car.turn_off()


