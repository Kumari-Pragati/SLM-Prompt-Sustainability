import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Missing_Positive([3, 4, -1, 1, 5], 5), 2)
        self.assertEqual(first_Missing_Positive([1, 2, 0], 3), 3)
        self.assertEqual(first_Missing_Positive([-3, -1, 0, 2, 4], 5), 1)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 6, 7, 8, 0, 10], 9), 5)

    def test_edge_case(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)
        self.assertEqual(first_Missing_Positive([0], 1), 1)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6], 6), 7)

    def test_boundary_case(self):
        self.assertEqual(first_Missing_Positive([-1], 1), 1)
        self.assertEqual(first_Missing_Positive([0, 0], 2), 1)
        self.assertEqual(first_Missing_Positive([1, 1], 2), 2)
        self.assertEqual(first_Missing_Positive([n for n in range(100)], 100), 101)
