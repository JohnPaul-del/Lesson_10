from abc import ABC, abstractmethod


class Clothes:
    @abstractmethod
    def fabric_count(self):
        pass


class Coat(Clothes):
    def fabric_count(self, coat_size):
        print(f"You need {round((coat_size/6.5+0.5), 2)} fabrics for a size {coat_size} coat ")


class Suite(Clothes):
    def fabric_count(self, stature):
        print(f"You need {stature*2 + 0.3} fabrics for a suit with stature {stature} ")


coat_1 = Coat()
coat_1.fabric_count(56)

suite_1 = Suite()
suite_1.fabric_count(170)