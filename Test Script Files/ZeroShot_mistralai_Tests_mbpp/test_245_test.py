import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum([1], 0), 1)

    def test_simple_array(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 15)

    def test_negative_numbers(self):
        self.assertEqual(max_sum([-1, -2, -3, -4, -5], 5), 15)

    def test_large_array(self):
        self.assertEqual(max_sum([1000, 2000, 3000, 4000, 5000], 5), 15000)
