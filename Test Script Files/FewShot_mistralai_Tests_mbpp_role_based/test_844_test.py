import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(get_Number(5, 3), 3)
        self.assertEqual(get_Number(10, 6), 8)

    def test_empty_list(self):
        self.assertEqual(get_Number(0, 1), 0)

    def test_invalid_input_k_greater_than_n(self):
        self.assertRaises(IndexError, get_Number, 5, 6)

    def test_invalid_input_k_less_than_1(self):
        self.assertRaises(ValueError, get_Number, 5, 0)

    def test_invalid_input_n_less_than_1(self):
        self.assertRaises(ValueError, get_Number, 0, 1)
