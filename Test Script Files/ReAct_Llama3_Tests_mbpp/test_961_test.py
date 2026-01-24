import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_edge_cases(self):
        self.assertEqual(roman_to_int(''), 0)
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_subtraction_cases(self):
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_invalid_roman_numerals(self):
        with self.assertRaises(KeyError):
            roman_to_int('abc')
        with self.assertRaises(KeyError):
            roman_to_int('IIII')
