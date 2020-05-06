class Person:

    def __init__(self, name):
        self.name = name

    def move(self):
        print('I am walking')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print('I am moving on bycicle')


def main():
    person = Person('David')
    person.move()

    cyclist = Cyclist('Daniel')
    cyclist.move()


if __name__ == '__main__':
    main()