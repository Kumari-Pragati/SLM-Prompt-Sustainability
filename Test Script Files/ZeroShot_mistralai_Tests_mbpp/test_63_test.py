import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_difference([1]), 0)

    def test_two_elements_list(self):
        self.assertEqual(max_difference([1, 2]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_difference([-1, -2]), 3)

    def test_positive_numbers(self):
        self.assertEqual(max_difference([1, 2]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(max_difference([-1, 1, 2]), 2)

    def test_large_numbers(self):
        self.assertEqual(max_difference([1000000001, 1000000002]), 1)
