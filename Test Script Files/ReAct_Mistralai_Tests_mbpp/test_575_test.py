import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_count_no_positive(self):
        """Test count_no with positive inputs"""
        self.assertEqual(count_no(2, 5, 1, 10), 5)
        self.assertEqual(count_no(3, 3, 3, 3), 3)
        self.assertEqual(count_no(5, 10, 1, 100), 100)

    def test_count_no_zero(self):
        """Test count_no with zero as divisor"""
        self.assertEqual(count_no(2, 5, 1, 0), 0)
        self.assertEqual(count_no(0, 5, 1, 10), 10)

    def test_count_no_negative(self):
        """Test count_no with negative inputs"""
        self.assertEqual(count_no(-2, 5, -10, -1), -9)
        self.assertEqual(count_no(-3, 3, -3, -3), -3)
        self.assertEqual(count_no(-5, 10, -1, -100), -100)

    def test_count_no_out_of_range(self):
        """Test count_no with out-of-range inputs"""
        self.assertRaises(IndexError, count_no, 2, 5, 0, -1)
        self.assertRaises(IndexError, count_no, 2, 5, 11, 10)

    def test_count_no_invalid_N(self):
        """Test count_no with invalid N (count exceeds range)"""
        self.assertRaises(ValueError, count_no, 2, 11, 1, 10)
