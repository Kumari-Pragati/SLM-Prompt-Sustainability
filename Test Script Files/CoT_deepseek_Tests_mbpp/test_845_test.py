import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Digits(1234), 4)

    def test_single_digit(self):
        self.assertEqual(find_Digits(5), 1)

    def test_negative_number(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Digits(0), 1)
        self.assertEqual(find_Digits(1), 1)

    def test_large_number(self):
        self.assertEqual(find_Digits(1000000000), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Digits('abc')
