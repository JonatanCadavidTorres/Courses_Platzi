class Washing_machine:

    def __init__(self):
        pass

    def wash(self, temperature='hot'):
        self._fill_tanq_of_water(temperature)
        self._add_soap()
        self._wash()
        self._dry()

    def _fill_tanq_of_water(self, temperature):
        print(f'Filling the tanq with water {temperature}')

    def _add_soap(self):
        print('adding soap')

    def _wash(self):
        print('washing clothes')

    def _dry(self):
        print('drying clothes')


if __name__ == '__main__':
    washing_machine = Washing_machine()
    washing_machine.wash()