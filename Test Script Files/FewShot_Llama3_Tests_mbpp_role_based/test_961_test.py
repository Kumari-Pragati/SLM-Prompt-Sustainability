import unittest
from mbpp_961_code import roman_to_int

class TestRomanToInt(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(roman_to_int('III'), 3)

    def test_edge_case(self):
        self.assertEqual(roman_to_int('IV'), 4)

    def test_subtraction_case(self):
        self.assertEqual(roman_to_int('IX'), 9)

    def test_multiple_subtraction_case(self):
        self.assertEqual(roman_to_int('IVX'), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            roman_to_int('abc')

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            roman_to_int('')
