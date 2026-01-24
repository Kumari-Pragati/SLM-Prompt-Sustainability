import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_equal([(1, 2), (3, 4), (5, 6)], 2), "All tuples have same length")

    def test_edge_case_empty_list(self):
        self.assertEqual(get_equal([], 2), "All tuples do not have same length")

    def test_boundary_case_one_tuple(self):
        self.assertEqual(get_equal([(1, 2)], 2), "All tuples have same length")
        self.assertEqual(get_equal([(1, 2)], 1), "All tuples do not have same length")

    def test_corner_case_different_length_tuples(self):
        self.assertEqual(get_equal([(1, 2), (3, 4, 5)], 2), "All tuples do not have same length")

    def test_invalid_input_non_tuple_elements(self):
        with self.assertRaises(TypeError):
            get_equal([1, 2, 3], 2)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(ValueError):
            get_equal([(1, 2), (3, 4)], -1)
