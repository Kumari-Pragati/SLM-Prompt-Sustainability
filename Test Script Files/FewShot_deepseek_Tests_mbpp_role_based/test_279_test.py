import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(is_num_decagonal(1), 1)
        self.assertEqual(is_num_decagonal(2), 10)
        self.assertEqual(is_num_decagonal(3), 37)

    def test_zero(self):
        self.assertEqual(is_num_decagonal(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(is_num_decagonal(-1), -1)
        self.assertEqual(is_num_decagonal(-2), -10)

    def test_large_numbers(self):
        self.assertEqual(is_num_decagonal(100), 39900)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
