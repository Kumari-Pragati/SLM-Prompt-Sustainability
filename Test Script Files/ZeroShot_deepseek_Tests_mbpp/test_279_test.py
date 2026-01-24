import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(is_num_decagonal(1), 1)
        self.assertEqual(is_num_decagonal(2), 10)
        self.assertEqual(is_num_decagonal(3), 35)
        self.assertEqual(is_num_decagonal(4), 84)
        self.assertEqual(is_num_decagonal(5), 155)

    def test_negative_numbers(self):
        self.assertEqual(is_num_decagonal(-1), -4)
        self.assertEqual(is_num_decagonal(-2), -15)
        self.assertEqual(is_num_decagonal(-3), -34)
        self.assertEqual(is_num_decagonal(-4), -63)
        self.assertEqual(is_num_decagonal(-5), -100)

    def test_zero(self):
        self.assertEqual(is_num_decagonal(0), 0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_num_decagonal(1.5)

    def test_large_numbers(self):
        self.assertEqual(is_num_decagonal(100), 39900)
        self.assertEqual(is_num_decagonal(1000), 39999000)
