import unittest
from mbpp_249_code import intersection_array

class TestIntersectionArray(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(intersection_array([], []), [])

    def test_single_element_inputs(self):
        self.assertEqual(intersection_array([1], [1]), [1])
        self.assertEqual(intersection_array([1], [2]), [])

    def test_common_elements(self):
        self.assertEqual(intersection_array([1, 2, 3], [2, 3, 4]), [2, 3])

    def test_no_common_elements(self):
        self.assertEqual(intersection_array([1, 2, 3], [4, 5, 6]), [])

    def test_duplicates(self):
        self.assertEqual(intersection_array([1, 2, 2], [1, 2, 2]), [1, 2])

    def test_duplicates_in_second_array(self):
        self.assertEqual(intersection_array([1, 2, 3], [1, 2, 2, 3]), [1, 2, 3])

    def test_duplicates_in_first_array(self):
        self.assertEqual(intersection_array([1, 1, 2, 3], [1, 2, 3]), [1, 2, 3])
