import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(min_difference([1]), 0)

    def test_two_elements_list(self):
        self.assertEqual(min_difference([1, 2]), 1)

    def test_three_elements_list(self):
        self.assertEqual(min_difference([1, 2, 3]), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_difference([-1, -2, -3]), 1)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(min_difference([1, -2, 3]), 1)

    def test_duplicates(self):
        self.assertEqual(min_difference([1, 1, 2]), 0)

    def test_large_numbers(self):
        self.assertEqual(min_difference([1000000001, 1000000002, 1000000003]), 1)
