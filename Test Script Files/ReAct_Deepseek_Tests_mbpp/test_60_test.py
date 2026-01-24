import unittest
from mbpp_60_code import max_len_sub

class TestMaxLenSub(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, 15, 20, 25, 30]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 5)

    def test_edge_case_single_element(self):
        arr = [10]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 1)

    def test_edge_case_empty_array(self):
        arr = []
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 0)

    def test_edge_case_decreasing_sequence(self):
        arr = [30, 25, 20, 15, 10]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 5)

    def test_typical_case_with_duplicates(self):
        arr = [10, 15, 20, 20, 30]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 3)

    def test_typical_case_with_difference_greater_than_one(self):
        arr = [10, 16, 20, 25, 30]
        n = len(arr)
        self.assertEqual(max_len_sub(arr, n), 4)
