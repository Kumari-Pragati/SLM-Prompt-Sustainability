import unittest
from mbpp_404_code import minimum

class TestMinimum(unittest.TestCase):

    def test_minimum_positive_numbers(self):
        """Test minimum function with positive numbers"""
        self.assertEqual(minimum(1, 2), 1)
        self.assertEqual(minimum(2, 1), 1)
        self.assertEqual(minimum(5, 3), 3)
        self.assertEqual(minimum(3, 5), 3)

    def test_minimum_zero_and_positive_numbers(self):
        """Test minimum function with zero and positive numbers"""
        self.assertEqual(minimum(0, 1), 0)
        self.assertEqual(minimum(1, 0), 0)
        self.assertEqual(minimum(0, 5), 0)
        self.assertEqual(minimum(5, 0), 0)

    def test_minimum_negative_numbers(self):
        """Test minimum function with negative numbers"""
        self.assertEqual(minimum(-1, -2), -1)
        self.assertEqual(minimum(-2, -1), -1)
        self.assertEqual(minimum(-5, -3), -3)
        self.assertEqual(minimum(-3, -5), -3)

    def test_minimum_mixed_numbers(self):
        """Test minimum function with mixed numbers"""
        self.assertEqual(minimum(-1, 1), -1)
        self.assertEqual(minimum(1, -1), -1)
        self.assertEqual(minimum(-5, 3), -5)
        self.assertEqual(minimum(3, -5), -5)

    def test_minimum_same_number(self):
        """Test minimum function with the same number"""
        self.assertEqual(minimum(1, 1), 1)
        self.assertEqual(minimum(-1, -1), -1)
