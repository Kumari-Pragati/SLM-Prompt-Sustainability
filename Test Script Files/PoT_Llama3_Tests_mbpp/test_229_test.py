import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange_array(arr, n), expected)

    def test_edge_case_negative(self):
        arr = [1, -2, 3, 4, 5]
        n = 5
        expected = [1, -2, 3, 4, 5]
        self.assertEqual(re_arrange_array(arr, n), expected)

    def test_edge_case_positive(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange_array(arr, n), expected)

    def test_edge_case_zero(self):
        arr = [1, 2, 3, 4, 5]
        n = 0
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange_array(arr, n), expected)

    def test_edge_case_empty(self):
        arr = []
        n = 0
        expected = []
        self.assertEqual(re_arrange_array(arr, n), expected)

    def test_edge_case_single_element(self):
        arr = [1]
        n = 1
        expected = [1]
        self.assertEqual(re_arrange_array(arr, n), expected)

    def test_edge_case_single_negative(self):
        arr = [-1]
        n = 1
        expected = [-1]
        self.assertEqual(re_arrange_array(arr, n), expected)

    def test_edge_case_single_positive(self):
        arr = [1]
        n = 1
        expected = [1]
        self.assertEqual(re_arrange_array(arr, n), expected)
