import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_difference([1, 2, 3, 4, 5]), 4)
        self.assertEqual(max_difference([-1, 0, 1, 2, 3]), 4)
        self.assertEqual(max_difference([0, 0, 0, 0, 0]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_difference([1]), 0)
        self.assertEqual(max_difference([-1]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(max_difference([-5, -4, -3, -2, -1]), 6)
        self.assertEqual(max_difference([-5, -4, -3, -2, -1, -2]), 4)
