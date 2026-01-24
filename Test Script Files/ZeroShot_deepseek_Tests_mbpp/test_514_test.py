import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_sum_elements_with_positive_numbers(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_sum_elements_with_negative_numbers(self):
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_sum_elements_with_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3)), 2)

    def test_sum_elements_with_zero(self):
        self.assertEqual(sum_elements((0, 0, 0)), 0)

    def test_sum_elements_with_single_number(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_sum_elements_with_empty_tuple(self):
        self.assertEqual(sum_elements(()), 0)
