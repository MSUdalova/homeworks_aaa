import json


class BaseAdvert:
    """
    Класс, эĸземпляры ĸоторого позволяют обращаться ĸ полям через точĸу
    """
    def __init__(self, advert: dict):
        for key, value in advert.items():
            if isinstance(value, dict):
                self.__dict__[key] = Advert(value)
            else:
                self.__dict__[key] = value

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class ColorizeMixin:
    """
    Миксин меняющий цвет объявления при выводе
    """
    repr_color_code = 33

    def __repr__(self):
        txt = super().__repr__()
        return f"\033[1;{self.repr_color_code};40m {txt}  \n"


class Advert(ColorizeMixin, BaseAdvert):

    def __init__(self, advert: dict):
        super(Advert, self).__init__(advert)

    def __getattribute__(self, name):
        if name == 'price' and object.__getattribute__(self, name) < 0:
            raise ValueError('price must be >= 0')
        else:
            return object.__getattribute__(self, name)

    def __getattr__(self, item):
        if item == 'price':
            return 0
        elif item == 'title':
            raise ValueError('title cannot be empty')

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('price must be >= 0')


if __name__ == '__main__':
    advert_js = """{
    "title": "python",
    "price": 1000,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""

    advert_d = json.loads(advert_js)
    advert = Advert(advert_d)
    print(advert)
