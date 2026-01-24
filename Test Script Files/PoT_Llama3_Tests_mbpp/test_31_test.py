import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 2), [3, 4])

    def test_edge_case_k_zero(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 0), [])

    def test_edge_case_k_equal_to_length(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 3), [3, 4, 5])

    def test_edge_case_k_greater_than_length(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 5), [3, 4, 5])

    def test_edge_case_empty_input(self):
        self.assertEqual(func([], 2), [])

    def test_edge_case_single_row(self):
        self.assertEqual(func([[1, 2, 3]], 2), [2, 3])

    def test_edge_case_single_element(self):
        self.assertEqual(func([[1]], 1), [1])

    def test_edge_case_k_one(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1), [5])

    def test_edge_case_k_equal_to_one(self):
        self.assertEqual(func([[1, 2, 3], [2, 3, 4], [3, 4, 5]], 1), [5])
