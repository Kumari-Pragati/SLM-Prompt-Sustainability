import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_empty_list(self):
        """Test re_order on an empty list"""
        result = re_order([])
        self.assertListEqual(result, [])

    def test_single_element(self):
        """Test re_order on a list with one element"""
        result = re_order([1])
        self.assertListEqual(result, [1])

    def test_multiple_elements(self):
        """Test re_order on a list with multiple elements"""
        result = re_order([3, 1, 4, 1, 5, 9, 2, 6])
        self.assertListEqual(result, [3, 1, 4, 1, 5, 9, 2, 6, 0, 0, 0, 0])

    def test_all_zero(self):
        """Test re_order on a list of zeros"""
        result = re_order([0] * 10)
        self.assertListEqual(result, [0] * 10)

    def test_negative_numbers(self):
        """Test re_order with negative numbers"""
        result = re_order([-3, 1, -4, 1, 5, -9, 2, 6])
        self.assertListEqual(result, [1, -3, 1, -4, 5, -9, 2, 6, 0, 0, 0, 0])

    def test_float_numbers(self):
        """Test re_order with float numbers"""
        result = re_order([3.14, 1, 4, 1, 5, 9, 2, 6])
        self.assertListEqual(result, [3.14, 1, 4, 1, 5, 9, 2, 6, 0, 0, 0, 0])

    def test_mixed_types(self):
        """Test re_order with mixed types"""
        result = re_order([3, "a", 1, None, 4, 1, 5, 9, 2, 6])
        self.assertListEqual(result, [3, "a", 1, None, 4, 1, 5, 9, 2, 6, 0, 0])
