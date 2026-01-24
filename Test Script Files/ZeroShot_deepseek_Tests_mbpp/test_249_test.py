import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_intersection_array(self):
        self.assertEqual(intersection_array([1,2,2,1],[2,2]), [2,2])
        self.assertEqual(intersection_array([4,9,5],[9,4,9,8,4]), [4,9])
        self.assertEqual(intersection_array([1,2,2,1],[1,1]), [1,1])
        self.assertEqual(intersection_array([],[1,2,3]), [])
        self.assertEqual(intersection_array([1,2,2,1],[2,2,1,1]), [2,2,1,1])
