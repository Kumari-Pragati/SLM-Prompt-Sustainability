import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [1, 3, 2, 4, 6, 5, 7, 8, 9, 10])

    def test_edge_case_all_positive(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [1, 3, 2, 4, 5])

    def test_edge_case_all_negative(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [-1, -3, -2, -4, -5])

    def test_edge_case_mixed_positive_negative(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [1, -2, 3, -4, 5])

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            re_arrange(arr, n)

    def test_invalid_input_non_integer_length(self):
        arr = [1, 2, 3, 4, 5]
        n ='string'
        with self.assertRaises(TypeError):
            re_arrange(arr, n)
