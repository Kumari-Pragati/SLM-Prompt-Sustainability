import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(max_difference([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_difference([-1, -2, -3, -4, -5]), 6)
        self.assertEqual(max_difference([0, 1, 2, 3, 4]), 4)

    def test_edge_cases(self):
        self.assertEqual(max_difference([1, 1]), 0)
        self.assertEqual(max_difference([-1, 1]), 2)
        self.assertEqual(max_difference([-1, -1]), 0)
        self.assertEqual(max_difference([1, -1]), 2)

    def test_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_difference([1]), 0)
        self.assertEqual(max_difference([-1]), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_difference([-5, -3, -2, -1]), 4)

    def test_positive_numbers(self):
        self.assertEqual(max_difference([1, 3, 5, 7]), 6)

    def test_mixed_numbers(self):
        self.assertEqual(max_difference([-5, 3, -2, 1]), 7)
