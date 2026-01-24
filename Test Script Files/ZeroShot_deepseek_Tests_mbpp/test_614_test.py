import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_single_number(self):
        self.assertEqual(cummulative_sum([1]), 1)

    def test_multiple_numbers(self):
        self.assertEqual(cummulative_sum([1, 2, 3]), 6)

    def test_nested_lists(self):
        self.assertEqual(cummulative_sum([[1, 2], [3, 4]]), 10)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            cummulative_sum([1, '2', 3])

    def test_negative_numbers(self):
        self.assertEqual(cummulative_sum([-1, -2, -3]), -6)

    def test_float_numbers(self):
        self.assertEqual(cummulative_sum([1.5, 2.5]), 4.0)
