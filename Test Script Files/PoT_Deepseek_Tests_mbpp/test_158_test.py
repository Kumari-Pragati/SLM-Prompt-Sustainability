import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_Ops([1, 1, 1], 3, 2), 1)

    def test_edge_case_with_single_element(self):
        self.assertEqual(min_Ops([5], 1, 10), 0)

    def test_boundary_case_with_max_value(self):
        self.assertEqual(min_Ops([10, 10, 10], 3, 10), 3)

    def test_invalid_input_with_negative_values(self):
        self.assertEqual(min_Ops([-1, -2, -3], 3, 2), -1)

    def test_invalid_input_with_non_integer_values(self):
        self.assertEqual(min_Ops([1.5, 2.5, 3.5], 3, 2), -1)

    def test_invalid_input_with_non_positive_k(self):
        self.assertEqual(min_Ops([1, 2, 3], 3, 0), -1)

    def test_corner_case_with_large_numbers(self):
        self.assertEqual(min_Ops([10**6, 10**6, 10**6], 3, 10**6), 3)
