import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)
        self.assertEqual(roman_to_int('MD'), 1500)
        self.assertEqual(roman_to_int('MCD'), 1400)
        self.assertEqual(roman_to_int('CMXCIV'), 994)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)
        self.assertEqual(roman_to_int('MMMCMXCIV'), 3994)

    def test_special_cases(self):
        self.assertEqual(roman_to_int('IVX'), 4 + 5 + 10)
        self.assertEqual(roman_to_int('IXL'), 9 + 50)
        self.assertEqual(roman_to_int('XCVIII'), 10 + 5 + 50 + 8)
        self.assertEqual(roman_to_int('XLVIII'), 40 + 5)
        self.assertEqual(roman_to_int('XCII'), 90 + 2)
        self.assertEqual(roman_to_int('CDXLVIII'), 400 + 40 + 5)
        self.assertEqual(roman_to_int('CDXXXIII'), 400 + 20 + 33)
        self.assertEqual(roman_to_int('CMXCIX'), 900 + 99)
        self.assertEqual(roman_to_int('MCMXCIX'), 1000 + 99)
