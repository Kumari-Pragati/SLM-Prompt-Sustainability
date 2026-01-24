import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):

    def test_intersection_array_typical(self):
        self.assertEqual(intersection_array([1, 2, 3, 4], [2, 3, 5, 6]), [2, 3])

    def test_intersection_array_empty(self):
        self.assertEqual(intersection_array([1, 2, 3, 4], []), [])

    def test_intersection_array_single_element(self):
        self.assertEqual(intersection_array([1, 2, 3, 4], [1]), [1])

    def test_intersection_array_no_intersection(self):
        self.assertEqual(intersection_array([1, 2, 3, 4], [5, 6, 7, 8]), [])

    def test_intersection_array_duplicates(self):
        self.assertEqual(intersection_array([1, 2, 2, 3, 3, 4], [2, 2, 3, 3, 4, 5]), [2, 2, 3, 3, 4])

    def test_intersection_array_empty_input(self):
        self.assertEqual(intersection_array([], [1, 2, 3, 4]), [])

    def test_intersection_array_invalid_input(self):
        with self.assertRaises(TypeError):
            intersection_array("string", [1, 2, 3, 4])
