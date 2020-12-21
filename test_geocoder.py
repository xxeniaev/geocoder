import os
import unittest
from address import Address
from data_base_loader import DataBase
from cities_loader import CitiesLoader


class SpellcheckerTest(unittest.TestCase):
    def test_set_address(self):
        address = Address('Екатеринбург Тургенева 4')
        self.assertEqual(address.get_address(),
                         ('Екатеринбург', 'Тургенева', '4'))

        address = Address('Тургенева 4 Екатеринбург')
        self.assertEqual(address.get_address(),
                         ('Екатеринбург', 'Тургенева', '4'))

    def test_db_load_xml(self):
        db = DataBase('db.xml',
                      'https://overpass-api.de/api/map?bbox='
                      '60.5451,56.8069,60.6535,56.8721', True)
        self.assertTrue(db.check_xml())

    def test_db_check_xml(self):
        db = DataBase('db.xml',
                      'https://overpass-api.de/api/map?bbox='
                      '60.5451,56.8069,60.6535,56.8721', True)
        self.assertTrue(db.check_xml())

        os.remove('db.xml')
        self.assertFalse(db.check_xml())

    def test_cities_loader(self):
        self.assertEqual(CitiesLoader("test.txt").cities,
                         {'Екатеринбург', 'Москва', 'Санкт-Петербург',
                          'Казань'})
