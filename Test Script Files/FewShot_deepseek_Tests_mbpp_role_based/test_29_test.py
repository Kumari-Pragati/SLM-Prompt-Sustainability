import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_typical_case(self):
        arr = [20, 10, 20, 30, 10, 10]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 30)

    def test_edge_case(self):
        arr = [1, 1, 1, 1, 1, 1]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1)

    def test_boundary_case(self):
        arr = [1]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1)

    def test_invalid_input(self):
        arr = []
        arr_size = 0
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)
