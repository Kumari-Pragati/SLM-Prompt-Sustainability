import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_list([1, 2, 3]), 6)

    def test_edge_case_zero(self):
        self.assertEqual(multiply_list([0, 1, 2]), 0)

    def test_edge_case_negative(self):
        self.assertEqual(multiply_list([-1, 2, 3]), -3)

    def test_edge_case_single_element(self):
        self.assertEqual(multiply_list([5]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(multiply_list([]), 1)

    def test_edge_case_single_zero(self):
        self.assertEqual(multiply_list([0]), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(multiply_list([-1]), -1)

    def test_edge_case_multiple_zeros(self):
        self.assertEqual(multiply_list([0, 0, 0]), 0)

    def test_edge_case_multiple_negatives(self):
        self.assertEqual(multiply_list([-1, -2, -3]), -6)
