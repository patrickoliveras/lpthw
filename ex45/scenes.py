from food import *

class Scene(object):

    def enter(self):
        print("This scene hasn't been configured")

class PrincipalsOffice(Scene):
    pass

class SchoolYard(Scene):
    pass

class FoodOutlet(Scene):

    prices = {}

    def __init__(self, prices, distance, time):
        self.prices     = prices
        self.distance   = distance
        self.time       = time

    def enter(self):
        print("Food outlet hasn't been configured")


class OutsideFoodOutlet(FoodOutlet):

    prices = {}

    def enter(self):
        print("Outside food outlet hasn't been configured")


class DonaMaria(FoodOutlet):

    def __init__(self):
        super().__init__(
            prices = {
                'a': 5,
                'b': 2,
                'c': 2,
                'd': 4,
                'e': 3,
                'f': 2,
            },
            distance = 1,
            time = 4
        )


class SchoolCafeteria(FoodOutlet):

    def __init__(self):
        super().__init__(
            prices = {
                'a': 4,
                'b': 1.5,
                'c': 1.5,
                'd': 3,
                'e': 2,
                'f': 1.5,
            },
            distance = 1,
            time = 6
        )


class PoshMcGuiresSauteesAndCoffee(FoodOutlet):

    def __init__(self):
        super().__init__(
            prices = {
                'a': 7,
                'b': 3,
                'c': 3,
                'd': 6,
                'e': 5,
                'f': 3,
            },
            distance = 1,
            time = 1
        )


class JimsOverTheFenceFoodFriends(OutsideFoodOutlet):

    def __init__(self):
        super().__init__(
            prices = {
                'a': 2,
                'b': 0.5,
                'c': 0.5,
                'd': 2,
                'e': 0.5,
                'f': 0.5,
            },
            distance = 2,
            time = 6
        )


class TimsHouse(OutsideFoodOutlet):

    def __init__(self):
        super().__init__(
            prices = {
                'a': 0,
                'b': 0,
                'c': 0,
                'd': 0,
                'e': 0,
                'f': 0,
            },
            distance = 3,
            time = 10
        )


class Map(object):

    scenes = {
        'principals_office':                    PrincipalsOffice(),
        'dona_maria':                           DonaMaria(),
        'school_cafeteria':                     SchoolCafeteria(),
        'posh_mc_guires_sautees_and_coffee':    PoshMcGuiresSauteesAndCoffee(),
        'jims_over_the_fence_food_friends':     JimsOverTheFenceFoodFriends(),
        'tims_house':                           TimsHouse(),
        'school_yard':                          SchoolYard(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
