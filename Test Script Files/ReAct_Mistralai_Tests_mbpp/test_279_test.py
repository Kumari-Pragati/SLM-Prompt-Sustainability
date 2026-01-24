import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(is_num_decagonal(1), 3)
        self.assertEqual(is_num_decagonal(2), 13)
        self.assertEqual(is_num_decagonal(3), 39)
        self.assertEqual(is_num_decagonal(4), 105)
        self.assertEqual(is_num_decagonal(5), 193)

    def test_zero(self):
        self.assertEqual(is_num_decagonal(0), -3)

    def test_negative_numbers(self):
        self.assertEqual(is_num_decagonal(-1), -21)
        self.assertEqual(is_num_decagonal(-2), -61)
        self.assertEqual(is_num_decagonal(-3), -135)
        self.assertEqual(is_num_decagonal(-4), -231)
        self.assertEqual(is_num_decagonal(-5), -369)

    def test_large_numbers(self):
        self.assertEqual(is_num_decagonal(1000), 4000000003)
        self.assertEqual(is_num_decagonal(-1000), -4000000003)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_num_decagonal(3.14)
