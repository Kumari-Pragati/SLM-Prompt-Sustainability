import unittest
from mbpp_845_code import find_Digits

class TestFindDigits(unittest.TestCase):

    def test_negative_input(self):
        self.assertEqual(find_Digits(-1), 0)

    def test_zero_input(self):
        self.assertEqual(find_Digits(0), 1)

    def test_one_input(self):
        self.assertEqual(find_Digits(1), 1)

    def test_edge_case(self):
        self.assertEqual(find_Digits(10), 2)

    def test_large_input(self):
        self.assertEqual(find_Digits(100), 5)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_Digits(10.5)
