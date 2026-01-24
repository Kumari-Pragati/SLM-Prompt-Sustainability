import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):
    def test_simple_positive(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_simple_negative(self):
        arr = [-1, -2, -3, -4, -5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [-5, -4, -3, -2, -1])

    def test_edge_empty(self):
        arr = []
        n = 0
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [])

    def test_edge_single(self):
        arr = [1]
        n = 1
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1])

    def test_edge_zero(self):
        arr = [0, 0, 0]
        n = 3
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [0, 0, 0])

    def test_edge_max(self):
        arr = [10, 10, 10]
        n = 3
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [10, 10, 10])

    def test_edge_min(self):
        arr = [-10, -10, -10]
        n = 3
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [-10, -10, -10])

    def test_edge_mixed(self):
        arr = [1, -1, 2, -2, 3, -3]
        n = 6
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [-3, -2, -1, 1, 2, 3])
