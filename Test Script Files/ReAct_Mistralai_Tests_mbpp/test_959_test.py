import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_empty_list(self):
        """Test average of an empty list"""
        with self.assertRaises(ZeroDivisionError):
            Average([])

    def test_single_element(self):
        """Test average of a list with one element"""
        result = Average([3])
        self.assertEqual(result, 3)

    def test_positive_numbers(self):
        """Test average of a list with multiple positive numbers"""
        result = Average([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)

    def test_negative_numbers(self):
        """Test average of a list with multiple negative numbers"""
        result = Average([-1, -2, -3, -4, -5])
        self.assertEqual(result, 1.2)

    def test_mixed_numbers(self):
        """Test average of a list with both positive and negative numbers"""
        result = Average([1, -2, 3, -4, 5])
        self.assertEqual(result, 1.5)

    def test_floats(self):
        """Test average of a list with floats"""
        result = Average([1.1, 2.2, 3.3, 4.4, 5.5])
        self.assertEqual(result, 3.3)

    def test_list_with_zero(self):
        """Test average of a list with zero"""
        result = Average([0, 1, 2, 3, 4])
        self.assertEqual(result, 2)
