import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):
    def test_all_tuples_same_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3), (1, 2, 3)], 3), "All tuples have same length")

    def test_all_tuples_diff_length(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2), (1, 2, 3, 4)], 3), "All tuples do not have same length")

    def test_empty_input(self):
        self.assertEqual(get_equal([], 3), "All tuples do not have same length")

    def test_single_tuple(self):
        self.assertEqual(get_equal([(1, 2, 3)], 3), "All tuples have same length")

    def test_k_zero(self):
        with self.assertRaises(TypeError):
            get_equal([(1, 2, 3)], 0)

    def test_non_integer_k(self):
        with self.assertRaises(TypeError):
            get_equal([(1, 2, 3)], 'k')
