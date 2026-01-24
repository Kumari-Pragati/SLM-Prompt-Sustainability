import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_simple_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_empty_tuple(self):
        self.assertEqual(sum_elements(()), 0)

    def test_single_element_tuple(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_maximum_and_minimum_values(self):
        self.assertEqual(sum_elements((float('inf'), -float('inf'))), 0)
        self.assertEqual(sum_elements((float('-inf'), float('inf'))), 0)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(sum_elements((1, -1, 2, -2)), 0)

    def test_large_numbers(self):
        self.assertEqual(sum_elements((10**6, -10**6)), 0)
