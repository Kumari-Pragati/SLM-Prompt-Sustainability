import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_single_roman_numeral(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('L'), 50)
        self.assertEqual(roman_to_int('C'), 100)
        self.assertEqual(roman_to_int('D'), 500)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_edge_cases(self):
        self.assertEqual(roman_to_int(''), 0)
        self.assertEqual(roman_to_int('MMMM'), 4000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            roman_to_int(123)
        with self.assertRaises(TypeError):
            roman_to_int(123.45)
        with self.assertRaises(TypeError):
            roman_to_int(['I', 'V', 'X'])
        with self.assertRaises(TypeError):
            roman_to_int({'I': 1, 'V': 5, 'X': 10})
