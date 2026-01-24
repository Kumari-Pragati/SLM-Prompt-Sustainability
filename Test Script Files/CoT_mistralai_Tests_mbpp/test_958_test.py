import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(58), 'LVIII')
        self.assertEqual(int_to_roman(499), 'CDXCIX')
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')

    def test_zero_and_negative_numbers(self):
        self.assertEqual(int_to_roman(0), '')
        self.assertEqual(int_to_roman(-1), '')
        self.assertEqual(int_to_roman(-9), 'IX')
        self.assertEqual(int_to_roman(-40), 'XL')
        self.assertEqual(int_to_roman(-99), 'CXCIX')
        self.assertEqual(int_to_roman(-1000), 'M')
        self.assertEqual(int_to_roman(-3000), 'MMM')

    def test_large_numbers(self):
        self.assertEqual(int_to_roman(3999999), 'CCCMXCIXCMXCIX')
        self.assertEqual(int_to_roman(4000000), 'CD')
        self.assertEqual(int_to_roman(4000001), 'CDII')
