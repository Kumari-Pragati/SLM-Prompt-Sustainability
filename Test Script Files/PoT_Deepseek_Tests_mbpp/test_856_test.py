import unittest
from mbpp_856_code import find_Min_Swaps

class TestFindMinSwaps(unittest.TestCase):

    def test_typical_case(self):
        arr = [0, 1, 0, 1, 1, 0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 1)

    def test_edge_case_single_element(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_boundary_case_all_zeros(self):
        arr = [0, 0, 0, 0, 0]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_boundary_case_all_ones(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_corner_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 0)

    def test_corner_case_mixed_array(self):
        arr = [1, 0, 1, 0, 0, 1]
        n = len(arr)
        self.assertEqual(find_Min_Swaps(arr, n), 2)
