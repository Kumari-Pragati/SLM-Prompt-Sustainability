import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_Missing_Positive([1, 2, 0], 3), 3)
        self.assertEqual(first_Missing_Positive([3, 4, -1, 1], 4), 2)

    def test_edge_conditions(self):
        self.assertEqual(first_Missing_Positive([1], 1), 2)
        self.assertEqual(first_Missing_Positive([], 0), 1)
        self.assertEqual(first_Missing_Positive([-1, -2, -3], 3), 1)
        self.assertEqual(first_Missing_Positive([2, 3, 4], 3), 1)

    def test_complex_cases(self):
        self.assertEqual(first_Missing_Positive([1, 1, 1], 3), 2)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6], 6), 1)
        self.assertEqual(first_Missing_Positive([1, 2, 2, 3, 1, 1], 6), 4)
