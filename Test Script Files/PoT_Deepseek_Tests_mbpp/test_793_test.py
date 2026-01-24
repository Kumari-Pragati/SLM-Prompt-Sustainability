import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 5, 7, 9]
        x = 7
        n = len(arr)
        self.assertEqual(last(arr, x, n), 3)

    def test_edge_case_with_single_element(self):
        arr = [5]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case_with_no_element(self):
        arr = []
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_boundary_case_with_duplicate_elements(self):
        arr = [5, 5, 5, 5]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 3)

    def test_corner_case_with_repeated_elements(self):
        arr = [1, 2, 2, 2, 3]
        x = 2
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_corner_case_with_smallest_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_corner_case_with_largest_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_invalid_input_with_negative_number(self):
        arr = [1, 2, 3, 4, 5]
        x = -1
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_invalid_input_with_non_integer(self):
        arr = [1, 2, 3, 4, 5]
        x = 'a'
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)
