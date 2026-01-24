import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):
    def test_typical_case(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = 0
        right_element = 9
        self.assertEqual(smallest_missing(A, left_element, right_element), 10)

    def test_edge_case_left_greater(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = 10
        right_element = 9
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element)

    def test_edge_case_right_greater(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = 0
        right_element = 10
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element)

    def test_edge_case_equal_elements(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = 0
        right_element = 0
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element + 1)

    def test_empty_array(self):
        A = []
        left_element = 0
        right_element = 0
        with self.assertRaises(IndexError):
            smallest_missing(A, left_element, right_element)

    def test_single_element_array(self):
        A = [0]
        left_element = 0
        right_element = 0
        with self.assertRaises(IndexError):
            smallest_missing(A, left_element, right_element)
