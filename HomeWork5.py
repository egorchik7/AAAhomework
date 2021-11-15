import json
import keyword


class ColorizeMixin:
    repr_color_code = 33

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m' \
               f' {self.title} | {self.price} ₽'


class Base:
    def __repr__(self):
        return f' {self.title} | {self.price} ₽'


class Advert(ColorizeMixin, Base):
    """Основной класс,который динамически создает атрибуты экземпляра класса
     из атрибутов JSON обьекта"""

    def __init__(self, dictionary: dict):
        for key, value in dictionary.items():
            if keyword.iskeyword(key):
                if isinstance(value, dict):
                    setattr(self, key + '_', Advert(value))
                else:
                    setattr(self, key + '_', value)
            elif isinstance(value, dict):
                setattr(self, key, Advert(value))
            else:
                if key == 'price':
                    self._price = 0
                    self.price = value
                else:
                    setattr(self, key, value)

    @property
    def price(self):
        if '_price' not in self.__dict__.keys():
            return 0
        else:
            return self._price

    @price.setter
    def price(self, value: int):
        """Проверка цены на неотрицательность"""
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value


if __name__ == '__main__':

    dog = """{
        "title": "Вельш-корги",
        "class": "dogs",
        "price": 1000,
        "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
        }"""

    dict_ad = json.loads(dog)
    corgi = Advert(dict_ad)
    print(corgi.price)