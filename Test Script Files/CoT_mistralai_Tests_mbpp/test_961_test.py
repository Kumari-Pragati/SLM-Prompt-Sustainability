import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):
    def test_simple_roman_numbers(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('C'), 100)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_mixed_roman_numbers(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IVX'), 4 + 10 - 5)
        self.assertEqual(roman_to_int('IXL'), 9 + 50 - 10)
        self.assertEqual(roman_to_int('XLVIII'), 48)
        self.assertEqual(roman_to_int('XCII'), 92)
        self.assertEqual(roman_to_int('CDXXX'), 430)
        self.assertEqual(roman_to_int('CMXCIV'), 914)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, roman_to_int, '')
        self.assertRaises(ValueError, roman_to_int, 'A')
        self.assertRaises(ValueError, roman_to_int, 'IIII')
        self.assertRaises(ValueError, roman_to_int, 'VV')
        self.assertRaises(ValueError, roman_to_int, 'MMM')
