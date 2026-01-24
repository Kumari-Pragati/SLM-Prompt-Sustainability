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
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_boundary_cases(self):
        self.assertEqual(roman_to_int(''), 0)
        self.assertEqual(roman_to_int('I\n'), 1)
        self.assertEqual(roman_to_int('IIII'), 4)
        self.assertEqual(roman_to_int('VV'), 14)
        self.assertEqual(roman_to_int('XXXX'), 40)
        self.assertEqual(roman_to_int('IIIIX'), 14)
        self.assertEqual(roman_to_int('IIIIXL'), 54)
        self.assertEqual(roman_to_int('IIIIXC'), 94)
        self.assertEqual(roman_to_int('IIIIXCL'), 144)
        self.assertEqual(roman_to_int('IIIIXCD'), 494)
        self.assertEqual(roman_to_int('IIIIXCM'), 994)
        self.assertEqual(roman_to_int('IIIIXCML'), 1494)
