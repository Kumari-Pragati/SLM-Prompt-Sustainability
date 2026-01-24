import unittest
from mbpp_371_code import smallest_missing

class TestSmallestMissing(unittest.TestCase):
    def test_typical_use_case(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = 0
        right_element = 9
        self.assertEqual(smallest_missing(A, left_element, right_element), 10)

    def test_edge_case_left_greater_than_right(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = 10
        right_element = 5
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element)

    def test_edge_case_right_greater_than_left(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = 5
        right_element = 10
        self.assertEqual(smallest_missing(A, left_element, right_element), left_element)

    def test_invalid_input_type(self):
        A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        left_element = "a"
        right_element = 10
        with self.assertRaises(TypeError):
            smallest_missing(A, left_element, right_element)
