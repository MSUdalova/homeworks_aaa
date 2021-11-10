from abc import ABC, abstractmethod
import random


class BasePokemon:

    def __init__(self):
        self.poketype = None
        self.name = None

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmodjiMixin:
    emodji = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡',
    }

    def __init__(self):
        self.poketype = None

    def __str__(self):
        txt_pocketype = super().__str__()
        return txt_pocketype.replace(self.poketype, self.emodji[self.poketype])


class AnimeMon(ABC):

    @abstractmethod
    def inc_exp(self, value: int):
        pass

    @property
    @abstractmethod
    def exp(self):
        pass

    @exp.setter
    def exp(self, value):
        self.exp = value


class Pokemon(EmodjiMixin, BasePokemon, AnimeMon):
    def __init__(self, name: str, poketype: str):
        super().__init__()
        self.name = name
        self.poketype = poketype
        self.exp = 0

    def exp(self):
        return 0

    def inc_exp(self, value: int):
        self.exp += value


class Digimon(AnimeMon):
    def __init__(self, name: str):
        self.name = name
        self.exp = 0

    def exp(self):
        return 0

    def inc_exp(self, value: int):
        self.exp += value * 8


def train(obj: Pokemon or Digimon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - obj.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            obj.inc_exp(step_size)


agumon = Digimon(name='Agumon')
train(agumon)
print(agumon.exp)

bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
train(bulbasaur)
print(bulbasaur.exp)
