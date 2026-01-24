import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset(["a", "b", "c"], ["a", "b"]))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_subset([1, 2, 3], [1, 2, 4]))
        self.assertTrue(check_subset([], []))
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], []))
        self.assertTrue(check_subset(["a", "b", "c"], ["a", "b", "d"]))
        self.assertFalse(check_subset(["a", "b", "c"], ["a", "b", "d", "e"]))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, check_subset, 1, [1, 2])
        self.assertRaises(TypeError, check_subset, [1], "list2")
