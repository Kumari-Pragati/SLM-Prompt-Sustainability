import unittest
from mbpp_706_code import is_subset

class TestIsSubset(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(is_subset([1, 2, 3], 3, [1, 2, 3], 3))
        self.assertTrue(is_subset([1, 2, 3, 4], 4, [1, 2, 3], 3))
        self.assertTrue(is_subset([1, 2, 3, 4, 5], 5, [1, 2, 3, 4], 4))

    def test_edge_cases(self):
        self.assertTrue(is_subset([], 0, [], 0))
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3, 4], 4))
        self.assertFalse(is_subset([1, 2, 3, 4], 4, [1, 2, 3], 3))

    def test_special_cases(self):
        self.assertFalse(is_subset([1, 2, 3], 3, [1, 2, 3, 4, 5], 5))
        self.assertFalse(is_subset([1, 2, 3, 4, 5], 5, [1, 2, 3], 3))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_subset(None, 0, [1, 2, 3], 3)
        with self.assertRaises(TypeError):
            is_subset([1, 2, 3], 0, None, 3)
        with self.assertRaises(TypeError):
            is_subset(None, 0, None, 0)
