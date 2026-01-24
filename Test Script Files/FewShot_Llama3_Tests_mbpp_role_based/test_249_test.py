import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):
    def test_intersection_array_empty_lists(self):
        self.assertEqual(intersection_array([], []), [])

    def test_intersection_array_single_element_lists(self):
        self.assertEqual(intersection_array([1], [1]), [1])
        self.assertEqual(intersection_array([1], [2]), [])

    def test_intersection_array_multiple_elements_lists(self):
        self.assertEqual(intersection_array([1, 2, 3], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(intersection_array([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(intersection_array([1, 2, 3], [4, 5, 6]), [])

    def test_intersection_array_duplicates(self):
        self.assertEqual(intersection_array([1, 1, 2, 2, 3], [1, 2, 2, 3, 3]), [1, 2, 3])
