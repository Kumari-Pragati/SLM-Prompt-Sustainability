import unittest
from924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_positive_numbers(self):
        """Test max_of_two with positive numbers"""
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(10, 2), 10)
        self.assertEqual(max_of_two(1, 0), 1)

    def test_zero_and_positive_numbers(self):
        """Test max_of_two with zero and positive numbers"""
        self.assertEqual(max_of_two(0, 5), 5)
        self.assertEqual(max_of_two(0, 1), 1)

    def test_negative_numbers(self):
        """Test max_of_two with negative numbers"""
        self.assertEqual(max_of_two(-5, -3), -3)
        self.assertEqual(max_of_two(-10, -2), -2)
        self.assertEqual(max_of_two(-1, -5), -1)

    def test_equal_numbers(self):
        """Test max_of_two with equal numbers"""
        self.assertEqual(max_of_two(5, 5), 5)
        self.assertEqual(max_of_two(-5, -5), -5)
        self.assertEqual(max_of_two(0, 0), 0)

    def test_negative_and_positive_numbers(self):
        """Test max_of_two with negative and positive numbers"""
        self.assertEqual(max_of_two(-5, 3), 3)
        self.assertEqual(max_of_two(-1, 5), 5)
        self.assertEqual(max_of_two(-3, 1), 1)
