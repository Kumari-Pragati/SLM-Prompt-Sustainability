import unittest
from mbpp_34_code import find_missing

class TestFindMissing(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 7, 6, 8], 8), 7)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 8, 9], 9), 7)
        self.assertEqual(find_missing([1, 2, 3, 4, 6, 8, 9, 10], 10), 5)
        self.assertEqual(find_missing([1, 2, 3, 5, 6, 8, 9, 10], 10), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_missing([1, 2, 3], 3), 4)
        self.assertEqual(find_missing([1, 2, 3], 2), -1)
        self.assertEqual(find_missing([1, 2, 3], 1), -1)
        self.assertEqual(find_missing([1, 2, 3], 0), -1)
        self.assertEqual(find_missing([1, 2, 3], 4), -1)

        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), 1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), -1)

    def test_special_cases(self):
        self.assertEqual(find_missing([1, 3, 5], 3), 2)
        self.assertEqual(find_missing([1, 2, 4], 3), -1)
        self.assertEqual(find_missing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), -1)
