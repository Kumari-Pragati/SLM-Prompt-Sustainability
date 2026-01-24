import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(roman_to_int('III'), 3)

    def test_edge_case(self):
        self.assertEqual(roman_to_int('IV'), 4)

    def test_edge_case2(self):
        self.assertEqual(roman_to_int('IX'), 9)

    def test_edge_case3(self):
        self.assertEqual(roman_to_int('LVIII'), 58)

    def test_edge_case4(self):
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_edge_case5(self):
        self.assertEqual(roman_to_int('MMXXI'), 2021)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            roman_to_int('abc')

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            roman_to_int('')
