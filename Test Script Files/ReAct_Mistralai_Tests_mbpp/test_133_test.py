import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativeNum(unittest.TestCase):

    def test_empty_list(self):
        """Test sum_negativenum with an empty list"""
        self.assertEqual(sum_negativenum([]), 0)

    def test_all_positive(self):
        """Test sum_negativenum with a list of all positive numbers"""
        self.assertEqual(sum_negativenum([1, 2, 3, 4]), 0)

    def test_all_negative(self):
        """Test sum_negativenum with a list of all negative numbers"""
        self.assertEqual(sum_negativenum([-1, -2, -3, -4]), 10)

    def test_mixed_numbers(self):
        """Test sum_negativenum with a list of mixed numbers"""
        self.assertEqual(sum_negativenum([-1, 0, -2, 1, -3, 2]), -4)

    def test_zero(self):
        """Test sum_negativenum with a zero number"""
        self.assertEqual(sum_negativenum([0]), 0)

    def test_large_numbers(self):
        """Test sum_negativenum with large numbers"""
        self.assertEqual(sum_negativenum([-1000000, 999999]), -1000000)

    def test_float_numbers(self):
        """Test sum_negativenum with float numbers"""
        self.assertAlmostEqual(sum_negativenum([-1.5, 0.5, -2.5]), -4.0)
