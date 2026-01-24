import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3), "All tuples have same length")

    def test_edge_case_k_zero(self):
        self.assertEqual(get_equal([(1, 2, 3), (4, 5, 6)], 0), "All tuples do not have same length")

    def test_edge_case_k_one(self):
        self.assertEqual(get_equal([(1), (2)], 1), "All tuples have same length")

    def test_edge_case_k_large(self):
        self.assertEqual(get_equal([(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)), "All tuples have same length")

    def test_corner_case_empty_input(self):
        self.assertEqual(get_equal([], 3), "All tuples do not have same length")

    def test_corner_case_single_tuple(self):
        self.assertEqual(get_equal([(1, 2, 3)], 3), "All tuples have same length")

    def test_corner_case_single_tuple_k_zero(self):
        self.assertEqual(get_equal([(1, 2, 3)], 0), "All tuples do not have same length")

    def test_corner_case_single_tuple_k_one(self):
        self.assertEqual(get_equal([(1)], 1), "All tuples have same length")

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            get_equal([1, 2, 3], 3)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            get_equal([(1, 2, 3), (4, 5, 6)], 'k')
