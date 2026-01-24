import unittest
from mbpp_782_code import Odd_Length_Sum

class TestOddLengthSum(unittest.TestCase):

    def test_empty_list(self):
        """Test if function returns 0 for an empty list"""
        self.assertEqual(Odd_Length_Sum([]), 0)

    def test_single_element_list(self):
        """Test if function returns the correct sum for a list with one element"""
        self.assertEqual(Odd_Length_Sum([1]), 1)

    def test_even_length_list(self):
        """Test if function returns 0 for a list with an even number of elements"""
        self.assertEqual(Odd_Length_Sum([1, 2]), 0)

    def test_odd_length_list_with_zero(self):
        """Test if function correctly handles a list with zero as an element"""
        self.assertEqual(Odd_Length_Sum([0, 1, 2]), 3)

    def test_large_list(self):
        """Test if function correctly handles large lists"""
        large_list = [i for i in range(1000)]
        self.assertEqual(Odd_Length_Sum(large_list), 2499995000)

    def test_negative_numbers(self):
        """Test if function correctly handles negative numbers"""
        self.assertEqual(Odd_Length_Sum([1, -2, 3]), 1)

    def test_list_with_floats(self):
        """Test if function correctly handles lists with floats"""
        self.assertEqual(Odd_Length_Sum([1.1, 2.2, 3.3]), 1.1)
