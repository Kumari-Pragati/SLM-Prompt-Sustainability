import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(is_num_decagonal(1), 4)
        self.assertEqual(is_num_decagonal(2), 20)
        self.assertEqual(is_num_decagonal(3), 52)

    def test_zero(self):
        self.assertEqual(is_num_decagonal(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(is_num_decagonal(-1), -12)
        self.assertEqual(is_num_decagonal(-2), -28)

    def test_large_numbers(self):
        self.assertEqual(is_num_decagonal(10), 380)
        self.assertEqual(is_num_decagonal(100), 39600)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_num_decagonal(1.5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
