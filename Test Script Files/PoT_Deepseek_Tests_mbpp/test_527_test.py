import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        sum = 5
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_boundary_case_empty_array(self):
        arr = []
        n = len(arr)
        sum = 5
        self.assertEqual(get_pairs_count(arr, n, sum), 0)

    def test_corner_case_duplicate_elements(self):
        arr = [1, 2, 1, 2, 3, 4, 5]
        n = len(arr)
        sum = 3
        self.assertEqual(get_pairs_count(arr, n, sum), 2)

    def test_corner_case_large_array(self):
        arr = list(range(1, 1001))
        n = len(arr)
        sum = 1000
        self.assertEqual(get_pairs_count(arr, n, sum), 499500)
