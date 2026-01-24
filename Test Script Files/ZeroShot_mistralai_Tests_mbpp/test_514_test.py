import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_sum_elements_positive(self):
        self.assertEqual(sum_elements((1, 2, 3, 4)), 10)
        self.assertEqual(sum_elements((0, 0, 0, 0)), 0)
        self.assertEqual(sum_elements((-1, -2, -3, -4)), -10)

    def test_sum_elements_empty(self):
        self.assertEqual(sum_elements(()), 0)

    def test_sum_elements_single_element(self):
        self.assertEqual(sum_elements((5,)), 5)

    def test_sum_elements_negative_and_positive(self):
        self.assertEqual(sum_elements((1, -2, 3, -4)), 2)
