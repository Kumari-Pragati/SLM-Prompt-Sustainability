import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 7, 8], 7), 6)
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 8], 7), 5)
        self.assertEqual(find_missing([1, 2, 3, 5, 6, 7, 8], 7), 4)
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 9], 9), 5)
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 8, 9], 9), -1)

    def test_edge_case(self):
        self.assertEqual(find_missing([1, 2, 3], 3), 4)
        self.assertEqual(find_missing([1, 2, 3, 4], 4), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5], 5), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6], 6), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7], 7), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8], 8), 9)

    def test_corner_case(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 7, 9, 10], 10), 5)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 12)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), -1)
