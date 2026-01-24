import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset(['a', 'b', 'c'], ['a', 'b', 'c']))
        self.assertTrue(check_subset([1, 2, 3], [1, 3]))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(check_subset([], []))
        self.assertTrue(check_subset([1], []))
        self.assertFalse(check_subset([1, 2, 3], []))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_subset("not a list", [1, 2, 3])
        with self.assertRaises(TypeError):
            check_subset([1, 2, 3], "not a list")
        with self.assertRaises(TypeError):
            check_subset("not a list", "not a list")
