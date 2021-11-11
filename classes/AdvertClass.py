import json


class Advert:
    def __init__(self, advert):
        for key, value in advert.items():
            if isinstance(value, dict):
                self.__dict__[key] = Advert(value)
            else:
                if key == 'price':
                    if value < 0:
                        print('must be >= 0')
                        raise ValueError
                    else:
                        self.__dict__[key] = value
                else:
                    self.__dict__[key] = value

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    def __getattr__(self, item):
        if item == 'price':
            print(0)



lesson_str = """{
"title": "python",
"price": 110,
"location": {
"address": "город Москва, Лесная, 7",
"metro_stations": ["Белорусская"]
}
}"""



lesson = json.loads(lesson_str)
lesson_ad = Advert(lesson)
print(lesson_ad.class_)
