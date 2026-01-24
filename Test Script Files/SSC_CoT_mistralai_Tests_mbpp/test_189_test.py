import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(first_Missing_Positive([3, 4, -1, 1, 5], 5), 2)
        self.assertEqual(first_Missing_Positive([1, 2, 0], 3), 3)
        self.assertEqual(first_Missing_Positive([7, 8, 9, 1, 2, 3, 4, 6], 8), 5)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 10)

    def test_edge_cases(self):
        self.assertEqual(first_Missing_Positive([0, 0, 0], 3), 1)
        self.assertEqual(first_Missing_Positive([-1, -1, -1], 3), 1)
        self.assertEqual(first_Missing_Positive([1, 1, 1], 3), 2)
        self.assertEqual(first_Missing_Positive([1000000000, 1000000000, 1000000000], 3), 1)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 1000000000], 10), 11)

    def test_boundary_cases(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)
        self.assertEqual(first_Missing_Positive([1], 1), 2)
        self.assertEqual(first_Missing_Positive([2, 1], 2), 3)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 11)
        self.assertEqual(first_Missing_Positive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 12)
