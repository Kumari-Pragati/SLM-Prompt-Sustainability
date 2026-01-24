import unittest
from mbpp_98_code import multiply_num

class TestMultiplyNum(unittest.TestCase):

    def test_empty_list(self):
        """Test multiply_num with an empty list"""
        with self.assertRaises(ZeroDivisionError):
            multiply_num([])

    def test_single_number(self):
        """Test multiply_num with a single number"""
        self.assertEqual(multiply_num([5]), 5)

    def test_positive_numbers(self):
        """Test multiply_num with multiple positive numbers"""
        self.assertAlmostEqual(multiply_num([1, 2, 3, 4, 5]), 3.6)

    def test_negative_numbers(self):
        """Test multiply_num with multiple negative numbers"""
        self.assertAlmostEqual(multiply_num([-1, -2, -3, -4, -5]), 15)

    def test_mixed_numbers(self):
        """Test multiply_num with a mix of positive and negative numbers"""
        self.assertAlmostEqual(multiply_num([1, -2, 3, -4, 5]), 0.2)

    def test_zero_in_list(self):
        """Test multiply_num with a zero in the list"""
        self.assertEqual(multiply_num([0, 1, 2, 3, 4]), 1.2)
