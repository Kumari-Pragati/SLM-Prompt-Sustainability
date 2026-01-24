import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        """Test sum_even_odd with an empty list"""
        with self.assertRaises(StopIteration):
            sum_even_odd([])

    def test_single_even_number(self):
        """Test sum_even_odd with a list containing only an even number"""
        result = sum_even_odd([2])
        self.assertEqual(result, 2)

    def test_single_odd_number(self):
        """Test sum_even_odd with a list containing only an odd number"""
        result = sum_even_odd([3])
        self.assertEqual(result, 3)

    def test_mixed_numbers(self):
        """Test sum_even_odd with a list containing both even and odd numbers"""
        result = sum_even_odd([2, 3, 4, 5, 6])
        self.assertEqual(result, 14)

    def test_first_even_not_found(self):
        """Test sum_even_odd when the first even number is not found"""
        result = sum_even_odd([1, 3, 5, 7])
        self.assertEqual(result, -1)

    def test_first_odd_not_found(self):
        """Test sum_even_odd when the first odd number is not found"""
        result = sum_even_odd([0, 2, 4, 6])
        self.assertEqual(result, -1)

    def test_list_with_only_negative_numbers(self):
        """Test sum_even_odd with a list containing only negative numbers"""
        result = sum_even_odd([-2, -3, -4, -5])
        self.assertEqual(result, -11)
