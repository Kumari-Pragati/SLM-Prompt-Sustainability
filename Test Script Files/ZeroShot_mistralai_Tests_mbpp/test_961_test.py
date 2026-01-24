import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_roman_to_int_simple(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_roman_to_int_edge_cases(self):
        self.assertEqual(roman_to_int(''), 0)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)
        self.assertEqual(roman_to_int('MD'), 1500)
        self.assertEqual(roman_to_int('CDXLVIII'), 448)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)
