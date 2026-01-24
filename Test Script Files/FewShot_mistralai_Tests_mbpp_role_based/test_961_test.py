import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):
    def test_simple_roman(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_mixed_roman(self):
        self.assertEqual(roman_to_int('XIV'), 14)
        self.assertEqual(roman_to_int('CDXLVIII'), 448)
        self.assertEqual(roman_to_int('MDCCCLXXXIII'), 1783)

    def test_invalid_roman(self):
        self.assertRaises(ValueError, roman_to_int, 'XV')
        self.assertRaises(ValueError, roman_to_int, 'XLX')
        self.assertRaises(ValueError, roman_to_int, 'MMM')
