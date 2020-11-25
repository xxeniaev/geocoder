import unittest
from Address import Address


class SpellcheckerTest(unittest.TestCase):
    def test_set_address(self):
        address = Address()

        address.set_address('Екатеринбург Тургенева 4')
        self.assertEqual(address.get_address(),
                         ('Екатеринбург', 'Тургенева', '4'))
        address.set_address('Тургенева 4 Екатеринбург')
        self.assertEqual(address.get_address(),
                         ('Екатеринбург', 'Тургенева', '4'))
