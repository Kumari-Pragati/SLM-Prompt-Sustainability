import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(is_num_decagonal(1), 2)
        self.assertEqual(is_num_decagonal(2), 13)
        self.assertEqual(is_num_decagonal(3), 34)
        self.assertEqual(is_num_decagonal(4), 65)

    def test_zero(self):
        self.assertEqual(is_num_decagonal(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(is_num_decagonal(-1), -5)
        self.assertEqual(is_num_decagonal(-2), -14)
        self.assertEqual(is_num_decagonal(-3), -27)

    def test_large_numbers(self):
        self.assertEqual(is_num_decagonal(100), 39900)
        self.assertEqual(is_num_decagonal(200), 199000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
        with self.assertRaises(TypeError):
            is_num_decagonal(None)
