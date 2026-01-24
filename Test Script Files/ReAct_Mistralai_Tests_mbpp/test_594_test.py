import unittest
from mbpp_594_code import diff_even_odd

class TestDiffEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        """Test behavior with an empty list"""
        with self.assertRaises(StopIteration):
            diff_even_odd([])

    def test_single_even_number(self):
        """Test behavior with a single even number"""
        result = diff_even_odd([2])
        self.assertEqual(result, 2)

    def test_single_odd_number(self):
        """Test behavior with a single odd number"""
        result = diff_even_odd([1])
        self.assertEqual(result, -1)

    def test_mixed_list_even_first(self):
        """Test behavior with a list where an even number comes first"""
        result = diff_even_odd([2, 1])
        self.assertEqual(result, 1)

    def test_mixed_list_odd_first(self):
        """Test behavior with a list where an odd number comes first"""
        result = diff_even_odd([1, 2])
        self.assertEqual(result, -1)

    def test_all_even_numbers(self):
        """Test behavior with a list of all even numbers"""
        result = diff_even_odd([2, 4, 6])
        self.assertEqual(result, 2)

    def test_all_odd_numbers(self):
        """Test behavior with a list of all odd numbers"""
        result = diff_even_odd([1, 3, 5])
        self.assertEqual(result, -1)

    def test_list_with_zero(self):
        """Test behavior with a list containing zero"""
        result = diff_even_odd([0, 1])
        self.assertEqual(result, 1)
