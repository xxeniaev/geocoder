import re

from CitiesLoader import CitiesLoader


class Address:

    def __init__(self):
        super().__init__()
        self._city = ''
        self._street = ''
        self._house = ''

    def set_address(self, address_string: str):
        cities = CitiesLoader("test.txt").cities

        # надо в дальнейшем учитывать, что в адресе могут фигурировать
        # запятые, а также слова
        # "дом/д/д.", "улица/ул/ул./проспект", "город/г/г."
        # сделать английскую адаптацию
        address_list = address_string.split()

        # city
        # надо в дальнейшем учитывать, что может быть 2слова в названии города
        for i in address_list:
            if i in cities:
                self._city = i
                address_list.remove(self._city)

        # house
        # надо в дальнейшем учитывать, что цифра может быть также
        # в названии улицы
        pattern = re.compile('([1-9]+[а-я]*)')
        for e in address_list:
            if re.findall(pattern, e):
                self._house = re.findall(pattern, e)[0]
                address_list.remove(self._house)

        # street
        self._street = ' '.join(address_list)

    def get_address(self):
        return self._city, self._street, self._house
