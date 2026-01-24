import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        dep = [2, 3, 4, 5, 6]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 3)

    def test_edge_case_empty_array(self):
        arr = []
        dep = [1, 2, 3]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 1)

    def test_edge_case_empty_departure_array(self):
        arr = [1, 2, 3]
        dep = []
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 1)

    def test_edge_case_single_element_array(self):
        arr = [1]
        dep = [1]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 1)

    def test_edge_case_single_element_departure_array(self):
        arr = [1, 2, 3]
        dep = [1]
        n = len(arr)
        self.assertEqual(find_platform(arr, dep, n), 1)

    def test_invalid_input_array_length_mismatch(self):
        arr = [1, 2, 3]
        dep = [1, 2, 3, 4]
        n = len(arr)
        with self.assertRaises(IndexError):
            find_platform(arr, dep, n)
