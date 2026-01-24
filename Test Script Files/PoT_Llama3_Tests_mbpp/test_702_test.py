import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge_case_k_zero(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 4)

    def test_edge_case_k_equal_to_max(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 4), 1)

    def test_edge_case_k_greater_than_max(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 5), 1)

    def test_edge_case_k_negative(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, -1), 4)

    def test_edge_case_n_one(self):
        self.assertEqual(removals([1], 1, 1), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(removals([], 0, 1), 0)

    def test_corner_case_k_equal_to_key(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)

    def test_corner_case_k_greater_than_key(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 2), 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            removals('abc', 5, 1)

    def test_invalid_input_size(self):
        with self.assertRaises(TypeError):
            removals([1, 2, 3], 5, 1)
