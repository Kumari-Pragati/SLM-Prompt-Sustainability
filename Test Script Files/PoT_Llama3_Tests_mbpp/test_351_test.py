import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_case_k_zero(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 0), -1)

    def test_edge_case_k_equal_n(self):
        self.assertEqual(first_Element([1, 1, 1, 1, 1], 5, 5), 1)

    def test_edge_case_k_greater_n(self):
        self.assertEqual(first_Element([1, 2, 3, 4, 5], 5, 10), -1)

    def test_edge_case_n_zero(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_edge_case_n_one(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_edge_case_k_greater_n_and_n_one(self):
        self.assertEqual(first_Element([1], 1, 2), -1)
