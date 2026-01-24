import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(cummulative_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(cummulative_sum([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(cummulative_sum([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(cummulative_sum([1, -2, 3]), 4)

    def test_mixed_numbers(self):
        self.assertEqual(cummulative_sum([1, -2, 3, -4, 5]), 6)

    def test_list_with_zero(self):
        self.assertEqual(cummulative_sum([0, 1, 2, 3]), 6)

    def test_list_with_only_zero(self):
        self.assertEqual(cummulative_sum([0]), 0)

    def test_list_with_only_negative_numbers(self):
        self.assertEqual(cummulative_sum([-1, -2, -3]), 6)

    def test_list_with_only_floats(self):
        self.assertEqual(cummulative_sum([1.1, 2.2, 3.3]), 6.6)

    def test_list_with_mixed_floats_and_integers(self):
        self.assertEqual(cummulative_sum([1, 2.2, 3]), 6.2)

    def test_list_with_large_numbers(self):
        self.assertEqual(cummulative_sum([1000000001, 1000000002, 1000000003]), 3000000006)

    def test_list_with_small_negative_numbers(self):
        self.assertEqual(cummulative_sum([-1000000001, -1000000002, -1000000003]), -3000000006)
