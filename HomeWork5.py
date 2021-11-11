import json

corpus = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
    }"""

dict_corp = json.loads(corpus)


class ColorizeMixin:
    repr_color_code = 32

    def __repr__(self):
        return f'{self.title} | {self.price}'

    # def __setattr__(self, key, value):
    # self.__dict__[key] = value


class Advert:

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, Advert(value))

            else:
                if key == 'price':
                    self._price = 0
                    self.price = value
                else:
                    setattr(self, key, value)

    #     def __repr__(self):
    #         return f' {self.title} | {self.price}'

    @property
    def price(self):
        print('Getting price as attr')
        return self._price

    @price.setter
    def price(self, value):
        print('setter')
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value


A = Advert(dict_corp)
print(A.price)