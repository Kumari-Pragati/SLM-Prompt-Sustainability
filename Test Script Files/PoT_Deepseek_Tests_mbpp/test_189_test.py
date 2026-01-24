import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(first_Missing_Positive([1,2,0], 3), 3)
        self.assertEqual(first_Missing_Positive([3,4,-1,1], 4), 2)
        self.assertEqual(first_Missing_Positive([7,8,9,10,11,12], 6), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)
        self.assertEqual(first_Missing_Positive([1], 1), 2)
        self.assertEqual(first_Missing_Positive([2], 1), 1)
        self.assertEqual(first_Missing_Positive([-1, 0, 1, 2], 4), 3)

    def test_corner_cases(self):
        self.assertEqual(first_Missing_Positive([1, 1, 1, 1], 4), 2)
        self.assertEqual(first_Missing_Positive([-1, -1, -1, -1], 4), 1)
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4], 4), 5)
