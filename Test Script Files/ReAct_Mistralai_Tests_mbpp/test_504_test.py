import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_positive_integer(self):
        """Test sum_Of_Series with positive integers"""
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 8)
        self.assertEqual(sum_Of_Series(3), 81)
        self.assertEqual(sum_Of_Series(10), 2772)

    def test_zero(self):
        """Test sum_Of_Series with zero"""
        self.assertEqual(sum_Of_Series(0), 0)

    def test_negative_integer(self):
        """Test sum_Of_Series with negative integers"""
        self.assertEqual(sum_Of_Series(-1), -1)
        self.assertEqual(sum_Of_Series(-2), -64)
        self.assertEqual(sum_Of_Series(-3), -291)

    def test_large_positive_integer(self):
        """Test sum_Of_Series with large positive integers"""
        self.assertEqual(sum_Of_Series(100), 33550616)

    def test_large_negative_integer(self):
        """Test sum_Of_Series with large negative integers"""
        self.assertEqual(sum_Of_Series(-100), -33550616)

    def test_non_integer(self):
        """Test sum_Of_Series with non-integer values"""
        with self.assertRaises(TypeError):
            sum_Of_Series(3.14)
