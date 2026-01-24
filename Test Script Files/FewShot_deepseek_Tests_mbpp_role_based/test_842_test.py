import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):
    def test_typical_case(self):
        arr = [20, 10, 20, 30, 10, 10]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 30)

    def test_edge_case(self):
        arr = [10]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 10)

    def test_boundary_case(self):
        arr = [10, 10]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)

    def test_invalid_input(self):
        arr = [10, 20, 30]
        arr_size = -1
        with self.assertRaises(Exception):
            get_odd_occurence(arr, arr_size)
