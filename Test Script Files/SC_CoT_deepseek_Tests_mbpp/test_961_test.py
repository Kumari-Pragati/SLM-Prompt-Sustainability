import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInteger(unittest.TestCase):

    def test_typical_roman_numerals(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_boundary_conditions(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)

    def test_edge_cases(self):
        self.assertEqual(roman_to_int('MMMCMXCIX'), 3999)
        self.assertEqual(roman_to_int('MMMM'), 4000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            roman_to_int(1234)
        with self.assertRaises(ValueError):
            roman_to_int('IIII')
        with self.assertRaises(KeyError):
            roman_to_int('Z')
