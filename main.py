from address import Address
from data_base_loader import DataBase


def main():
    entrance = input('Ввод:\n')  # строка ввода данных
    address = Address(entrance)  # создаётся экземпляр класса Адрес
    print(address.get_address())  # задаются параметры адреса

    data_base = DataBase('db.xml',
                         'https://overpass-api.de/api/map?bbox='
                         '60.5451,56.8069,60.6535,56.8721', True)

    print('Вывод:\n')


if __name__ == '__main__':
    # geo_coder = GeoCoder()
    # geo_coder.start()
    main()
