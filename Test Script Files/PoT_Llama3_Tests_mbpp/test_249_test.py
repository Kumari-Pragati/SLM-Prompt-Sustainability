import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]), [4, 5])

    def test_edge_case_empty_array1(self):
        self.assertEqual(intersection_array([], [1, 2, 3, 4, 5]), [])

    def test_edge_case_empty_array2(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], []), [])

    def test_edge_case_single_element_array1(self):
        self.assertEqual(intersection_array([1], [1, 2, 3, 4, 5]), [1])

    def test_edge_case_single_element_array2(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [1]), [1])

    def test_edge_case_duplicates(self):
        self.assertEqual(intersection_array([1, 2, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7]), [2, 3, 4])

    def test_edge_case_duplicates_array1(self):
        self.assertEqual(intersection_array([1, 1, 2, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [1, 2, 3, 4])

    def test_edge_case_duplicates_array2(self):
        self.assertEqual(intersection_array([1, 2, 3, 4, 5], [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])
