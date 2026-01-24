import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(intersection_array([1,2,2,1], [2,2]), [2,2])

    def test_empty_array(self):
        self.assertEqual(intersection_array([], [2,2]), [])
        self.assertEqual(intersection_array([1,2,2,1], []), [])

    def test_single_element(self):
        self.assertEqual(intersection_array([1], [1]), [1])
        self.assertEqual(intersection_array([1], [2]), [])

    def test_duplicate_elements(self):
        self.assertEqual(intersection_array([1,2,2,1], [2,2]), [2,2])

    def test_no_intersection(self):
        self.assertEqual(intersection_array([1,2,3], [4,5,6]), [])

    def test_same_arrays(self):
        self.assertEqual(intersection_array([1,2,3], [1,2,3]), [1,2,3])
