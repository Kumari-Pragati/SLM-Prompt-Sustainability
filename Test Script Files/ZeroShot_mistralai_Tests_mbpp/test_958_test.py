import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(int_to_roman(0), '')

    def test_one(self):
        self.assertEqual(int_to_roman(1), 'I')

    def test_four(self):
        self.assertEqual(int_to_roman(4), 'IV')

    def test_nine(self):
        self.assertEqual(int_to_roman(9), 'IX')

    def test_forty(self):
        self.assertEqual(int_to_roman(40), 'XL')

    def test_ninety(self):
        self.assertEqual(int_to_roman(90), 'XC')

    def test_four_hundred(self):
        self.assertEqual(int_to_roman(400), 'CD')

    def test_nine_hundred(self):
        self.assertEqual(int_to_roman(900), 'CM')

    def test_one_thousand(self):
        self.assertEqual(int_to_roman(1000), 'M')

    def test_three_thousand(self):
        self.assertEqual(int_to_roman(3000), 'MMM')

    def test_four_thousand_nine_hundred_and_ninety_nine(self):
        self.assertEqual(int_to_roman(4999), 'IVMMMCMXCIX')
