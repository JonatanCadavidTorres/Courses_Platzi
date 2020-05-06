class Automobile:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'en_reposo'
        self._engine = Engine(cylinders=4)

    def speed_up(self, type='slow'):
        if type == 'fast':
            self._engine.inject_fuel(10)
        else:
            self._engine.inject_fuel(3)

        self._status = 'moving'


class Engine:

    def __init__(self, cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_fuel(self, cantidad):
        pass