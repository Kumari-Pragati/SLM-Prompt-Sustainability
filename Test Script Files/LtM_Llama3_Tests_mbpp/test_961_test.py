import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('L'), 50)
        self.assertEqual(roman_to_int('C'), 100)
        self.assertEqual(roman_to_int('D'), 500)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(roman_to_int(''), 0)
        self.assertEqual(roman_to_int('IIV'), 6)
        self.assertEqual(roman_to_int('XIV'), 14)
        self.assertEqual(roman_to_int('MCMXCIX'), 1999)

    def test_complex_and_corner_cases(self):
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('XL'), 40)
        self.assertEqual(roman_to_int('XC'), 90)
        self.assertEqual(roman_to_int('CD'), 400)
        self.assertEqual(roman_to_int('CM'), 900)
