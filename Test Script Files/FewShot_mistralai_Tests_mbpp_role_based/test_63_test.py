import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(max_difference([1, 2, 3, 4, 5]), 4)

    def test_negative_list(self):
        self.assertEqual(max_difference([-1, -2, -3, -4, -5]), 4)

    def test_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_difference([1]), 0)

    def test_duplicate_elements(self):
        self.assertEqual(max_difference([1, 1, 2]), 1)

    def test_reverse_order(self):
        self.assertEqual(max_difference([5, 4, 3, 2, 1]), 4)

    def test_large_numbers(self):
        self.assertEqual(max_difference([1000000001, 1000000000]), 1)

    def test_negative_and_positive(self):
        self.assertEqual(max_difference([-1, 1]), 2)
