import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_edge_cases(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)

    def test_boundary_cases(self):
        self.assertEqual(roman_to_int('MMMCMXCIX'), 3999)
        self.assertEqual(roman_to_int('MMMM'), 4000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            roman_to_int(123)
        with self.assertRaises(ValueError):
            roman_to_int('IIII')
        with self.assertRaises(ValueError):
            roman_to_int('VV')
        with self.assertRaises(ValueError):
            roman_to_int('XXXX')
        with self.assertRaises(ValueError):
            roman_to_int('LL')
        with self.assertRaises(ValueError):
            roman_to_int('CCCC')
        with self.assertRaises(ValueError):
            roman_to_int('DD')
        with self.assertRaises(ValueError):
            roman_to_int('MMMMM')
