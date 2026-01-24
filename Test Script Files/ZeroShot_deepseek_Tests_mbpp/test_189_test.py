import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_first_Missing_Positive(self):
        self.assertEqual(first_Missing_Positive([1,2,0], 3), 3)
        self.assertEqual(first_Missing_Positive([3,4,-1,1], 4), 2)
        self.assertEqual(first_Missing_Positive([7,8,9,10,11,12], 6), 1)
        self.assertEqual(first_Missing_Positive([1,1,1,1], 4), 2)
        self.assertEqual(first_Missing_Positive([-1,-2,-3,-4], 4), 1)
        self.assertEqual(first_Missing_Positive([1,2,3,4], 4), 5)
        self.assertEqual(first_Missing_Positive([1,2,3,5], 4), 4)
        self.assertEqual(first_Missing_Positive([1,2,3,4,5], 5), 6)
        self.assertEqual(first_Missing_Positive([1,2,3,4,6], 5), 5)
        self.assertEqual(first_Missing_Positive([1,2,3,4,7], 5), 5)
