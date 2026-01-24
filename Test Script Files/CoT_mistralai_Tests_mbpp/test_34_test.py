import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 7, 8], 7), 6)
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 8], 5), 4)
        self.assertEqual(find_missing([1, 2, 3, 5, 6, 7, 8], 4), 3)
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 9], 5), 8)

    def test_edge_case(self):
        self.assertEqual(find_missing([1, 2, 3], 3), 4)
        self.assertEqual(find_missing([1, 2, 3, 4], 4), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 5), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6], 6), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7], 7), -1)

    def test_boundary_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8], 9), 9)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), 11)

    def test_invalid_input(self):
        self.assertRaises(ValueError, find_missing, [1, 2, 3], 0)
        self.assertRaises(ValueError, find_missing, [], 0)
        self.assertRaises(ValueError, find_missing, [1], 1)
        self.assertRaises(ValueError, find_missing, [1, 2], 2)
        self.assertRaises(ValueError, find_missing, [1, 2, 3, 4, 5, 6, 7, 8], -1)
