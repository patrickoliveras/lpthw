from random import randint

class Person(object):

    name = None

    def __init__(self, name):
        self.name = name


class Classmate(Person):

    def __init__(self, name):
        super().__init__(name)
        self.status = randint(1,3)

    def get_tip(self):
        pass

class Spotter(Person):
    pass
