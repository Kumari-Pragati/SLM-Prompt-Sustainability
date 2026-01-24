import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(cummulative_sum([[1], [2], [3]]), 6)

    def test_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_single_list(self):
        self.assertEqual(cummulative_sum([[1]]), 1)

    def test_negative_numbers(self):
        self.assertEqual(cummulative_sum([[-1], [2], [-3]]), -2)

    def test_large_numbers(self):
        self.assertEqual(cummulative_sum([[1000000001], [2], [3]]), 1000000003)

    def test_mixed_types(self):
        self.assertRaises(TypeError, cummulative_sum, [[1], 'a', [2]])
