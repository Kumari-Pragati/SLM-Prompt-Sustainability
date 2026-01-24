import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):
    def test_typical_input(self):
        arr = [1, 2, -3, 4, -5, 6]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [1, 2, -3, -5, 4, 6])

    def test_edge_case_positive(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case_negative(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [-1, -2, -3, -4, -5])

    def test_edge_case_mixed(self):
        arr = [1, -2, 3, -4, 5]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [1, -2, 3, -4, 5])

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [1])

    def test_edge_case_empty(self):
        arr = []
        n = len(arr)
        result = re_arrange(arr, n)
        self.assertEqual(result, [])

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            re_arrange([1, 2, 3], 'a')

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            re_arrange(123, 5)
