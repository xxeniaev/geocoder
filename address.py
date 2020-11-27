import re

from cities_loader import CitiesLoader


class Address:

    def __init__(self, address_string: str):
        self.address_string = address_string
        self._city = ''
        self._street = ''
        self._house = ''
        self.parse_address()

    def parse_address(self):
        cities = CitiesLoader("test.txt").cities

        # надо в дальнейшем учитывать, что в адресе могут фигурировать
        # запятые, а также слова
        # "дом/д/д.", "улица/ул/ул./проспект", "город/г/г."
        # сделать английскую адаптацию
        address_list = self.address_string.split()

        # city
        # надо в дальнейшем учитывать, что может быть 2слова в названии города
        for element in address_list:
            if element in cities:
                self._city = element
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
