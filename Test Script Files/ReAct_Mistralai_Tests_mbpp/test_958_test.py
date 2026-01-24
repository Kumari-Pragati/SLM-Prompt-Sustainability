import unittest
from mbpp_958_code import int_to_roman

class TestIntToRoman(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(3), "III")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(5), "V")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(10), "X")
        self.assertEqual(int_to_roman(40), "XL")
        self.assertEqual(int_to_roman(50), "L")
        self.assertEqual(int_to_roman(90), "XC")
        self.assertEqual(int_to_roman(100), "C")
        self.assertEqual(int_to_roman(400), "CD")
        self.assertEqual(int_to_roman(500), "D")
        self.assertEqual(int_to_roman(900), "CM")
        self.assertEqual(int_to_roman(1000), "M")

    def test_zero_and_negative_numbers(self):
        self.assertEqual(int_to_roman(0), "")
        self.assertEqual(int_to_roman(-1), "")

    def test_large_numbers(self):
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")
        self.assertEqual(int_to_roman(4000), "MMM")
