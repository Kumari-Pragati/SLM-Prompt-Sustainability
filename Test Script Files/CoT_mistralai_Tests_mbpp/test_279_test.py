import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(is_num_decagonal(1), 3)
        self.assertEqual(is_num_decagonal(2), 12)
        self.assertEqual(is_num_decagonal(3), 39)
        self.assertEqual(is_num_decagonal(4), 90)
        self.assertEqual(is_num_decagonal(5), 165)

    def test_zero(self):
        self.assertEqual(is_num_decagonal(0), -3)

    def test_negative_numbers(self):
        self.assertEqual(is_num_decagonal(-1), -3)
        self.assertEqual(is_num_decagonal(-2), -12)
        self.assertEqual(is_num_decagonal(-3), -39)
        self.assertEqual(is_num_decagonal(-4), -90)
        self.assertEqual(is_num_decagonal(-5), -165)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_num_decagonal, 'not_a_number')
        self.assertRaises(TypeError, is_num_decagonal, 0.5)
