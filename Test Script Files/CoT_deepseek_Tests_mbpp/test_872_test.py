import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset(['a', 'b', 'c'], ['a', 'b', 'c']))
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))
        self.assertTrue(check_subset([], [1, 2, 3]))
        self.assertTrue(check_subset([1, 2, 3], []))

    def test_edge_cases(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset([1, 2, 3], [1, 2, 4]))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_subset("not a list", [1, 2, 3])
        with self.assertRaises(TypeError):
            check_subset([1, 2, 3], "not a list")
        with self.assertRaises(TypeError):
            check_subset("not a list", "not a list")
