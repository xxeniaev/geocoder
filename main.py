from Address import Address
import sys


def main():
    entrance = sys.argv
    del entrance[0]
    print('первоначальный список', entrance)
    address = Address()
    address.set_address(entrance)
    print(address.get_address())


if __name__ == '__main__':
    # geo_coder = GeoCoder()
    # geo_coder.start()
    main()
