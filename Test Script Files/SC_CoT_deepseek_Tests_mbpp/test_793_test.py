import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(last(arr, x, n), 2)

    def test_edge_case_smallest_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 1
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case_largest_element(self):
        arr = [1, 2, 3, 4, 5]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 4)

    def test_edge_case_single_element(self):
        arr = [5]
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), 0)

    def test_edge_case_empty_array(self):
        arr = []
        x = 5
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_edge_case_not_found(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        n = len(arr)
        self.assertEqual(last(arr, x, n), -1)

    def test_invalid_input_negative_number(self):
        arr = [1, 2, 3, 4, 5]
        x = -3
        n = len(arr)
        with self.assertRaises(Exception):
            last(arr, x, n)

    def test_invalid_input_string(self):
        arr = [1, 2, 3, 4, 5]
        x = "3"
        n = len(arr)
        with self.assertRaises(Exception):
            last(arr, x, n)
