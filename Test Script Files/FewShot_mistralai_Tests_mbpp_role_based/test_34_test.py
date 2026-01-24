import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 8], 7), 5)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 7, 8], 7), 6)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 8], 7), 7)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_missing([], 0), -1)
        self.assertEqual(find_missing([1], 1), -1)
        self.assertEqual(find_missing([1, 2], 2), -1)
        self.assertEqual(find_missing([1, 2, 3], 3), -1)
        self.assertEqual(find_missing([1, 2, 3, 4], 4), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 5), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6], 6), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7], 7), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8], 8), -1)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, find_missing, [], -1)
        self.assertRaises(ValueError, find_missing, [1], 0)
        self.assertRaises(ValueError, find_missing, [1, 2], -1)
        self.assertRaises(ValueError, find_missing, [1, 2, 3], 0)
        self.assertRaises(ValueError, find_missing, [1, 2, 3, 4], -1)
        self.assertRaises(ValueError, find_missing, [1, 2, 3, 4, 5], 0)
