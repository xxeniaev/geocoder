from Address import Address
from DataBaseLoader import DataBase


def main():
    entrance = input('Ввод:\n')  # строка ввода данных
    address = Address()  # создаётся экземпляр класса Адрес
    address.set_address(entrance)  # задаются параметры адреса

    data_base = DataBase('db.xml', 'https://overpass-api.de/api/map?bbox=60.5451,56.8069,60.6535,56.8721', True)

    print('Вывод:\n')


if __name__ == '__main__':
    # geo_coder = GeoCoder()
    # geo_coder.start()
    main()
