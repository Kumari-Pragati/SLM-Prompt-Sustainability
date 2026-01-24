import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(first_Missing_Positive([3, 4, -1, 1, 7], 5), 2)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4], 4), 5)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_edge_and_boundary(self):
        self.assertEqual(first_Missing_Positive([0, 0, 1, 2, 3], 4), 5)
        self.assertEqual(first_Missing_Positive([-1, -2, -3], 3), 1)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6], 6), 7)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7], 7), 8)

    def test_complex(self):
        self.assertEqual(first_Missing_Positive([1, 2, 0, 4], 4), 3)
        self.assertEqual(first_Missing_Positive([-1, 0, 1, 2, 3], 5), 6)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 10)
        self.assertEqual(first_Missing_Positive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 11)
