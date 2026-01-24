import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(cummulative_sum([[1, 2], [3, 4]]), 10)

    def test_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_single_number(self):
        self.assertEqual(cummulative_sum([[5]]), 5)

    def test_negative_numbers(self):
        self.assertEqual(cummulative_sum([[-1, 2], [3, -4]]), -1)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            cummulative_sum([[1, '2'], [3, 4]])

    def test_nested_empty_list(self):
        self.assertEqual(cummulative_sum([[], []]), 0)

    def test_nested_single_empty_list(self):
        self.assertEqual(cummulative_sum([[1], []]), 1)
