import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_simple_roman(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_edge_cases(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_mixed_cases(self):
        self.assertEqual(roman_to_int('IIII'), 4)
        self.assertEqual(roman_to_int('VIIII'), 7)
        self.assertEqual(roman_to_int('IIX'), 8)
        self.assertEqual(roman_to_int('IXI'), 11)
        self.assertEqual(roman_to_int('XLIX'), 49)
        self.assertEqual(roman_to_int('XLVIII'), 48)
        self.assertEqual(roman_to_int('XLC'), 40 + 100)
        self.assertEqual(roman_to_int('XCXC'), 90 + 90)
        self.assertEqual(roman_to_int('CDXCIX'), 400 + 19)
        self.assertEqual(roman_to_int('MCMXCIX'), 1999)
