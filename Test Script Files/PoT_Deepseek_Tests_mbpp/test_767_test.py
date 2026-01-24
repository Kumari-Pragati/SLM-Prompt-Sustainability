import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_Pairs_Count(arr, n, sum), 2)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        sum = 5
        self.assertEqual(get_Pairs_Count(arr, n, sum), 0)

    def test_corner_case_all_elements_sum_to_target(self):
        arr = [1, 1, 1, 1]
        n = len(arr)
        sum = 4
        self.assertEqual(get_Pairs_Count(arr, n, sum), 6)

    def test_corner_case_duplicate_elements(self):
        arr = [1, 2, 3, 2, 1]
        n = len(arr)
        sum = 4
        self.assertEqual(get_Pairs_Count(arr, n, sum), 2)

    def test_corner_case_negative_elements(self):
        arr = [-1, -2, 3, 2, 1]
        n = len(arr)
        sum = 1
        self.assertEqual(get_Pairs_Count(arr, n, sum), 1)
