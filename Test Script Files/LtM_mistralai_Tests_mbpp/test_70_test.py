import unittest
from mbpp_70_code import get_equal

class TestGetEqual(unittest.TestCase):

    def test_simple_equal_tuples(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2, 3), (1, 2, 3)], 3), ("All tuples have same length"))

    def test_simple_inequal_tuples(self):
        self.assertEqual(get_equal([(1, 2, 3), (1, 2), (1, 2, 3)], 3), ("All tuples do not have same length"))

    def test_empty_input(self):
        self.assertEqual(get_equal([], 3), ("All tuples do not have same length"))

    def test_single_tuple(self):
        self.assertEqual(get_equal([(1, 2, 3)], 3), ("All tuples have same length"))

    def test_zero_tuples(self):
        self.assertEqual(get_equal([], 0), ("All tuples have same length"))

    def test_negative_k(self):
        self.assertRaises(ValueError, get_equal, [(1, 2, 3)], -1)

    def test_non_tuple_input(self):
        self.assertRaises(TypeError, get_equal, [1, 2, 3], 3)
