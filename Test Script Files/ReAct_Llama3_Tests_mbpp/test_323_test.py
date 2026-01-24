import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, -3, 4, -5, 6]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, 2, -5, 4, -3, 6])

    def test_edge_case_zero(self):
        arr = [1, 2, 3, 4, 5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case_negative(self):
        arr = [-1, -2, -3, -4, -5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [-1, -2, -3, -4, -5])

    def test_edge_case_positive(self):
        arr = [1, 2, 3, 4, 5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case_mixed(self):
        arr = [1, -2, 3, -4, 5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, -2, 3, -4, 5])

    def test_edge_case_out_of_place(self):
        arr = [1, 2, -3, 4, -5, 6]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, 2, -5, 4, -3, 6])

    def test_edge_case_out_of_place_negative(self):
        arr = [-1, -2, -3, -4, -5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [-1, -2, -3, -4, -5])

    def test_edge_case_out_of_place_positive(self):
        arr = [1, 2, 3, 4, 5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case_out_of_place_mixed(self):
        arr = [1, -2, 3, -4, 5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, -2, 3, -4, 5])
