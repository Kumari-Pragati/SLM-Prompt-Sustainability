import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(cummulative_sum([1]), 1)

    def test_simple_list(self):
        self.assertEqual(cummulative_sum([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(cummulative_sum([-1, -2, -3]), 6)

    def test_mixed_numbers(self):
        self.assertEqual(cummulative_sum([1, -2, 3]), 2)
