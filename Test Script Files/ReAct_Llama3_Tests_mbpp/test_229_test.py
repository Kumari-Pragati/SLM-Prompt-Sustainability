import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):

    def test_positive_array(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, arr)

    def test_negative_array(self):
        arr = [-1, -2, -3, -4, -5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, sorted(arr))

    def test_mixed_array(self):
        arr = [1, -2, 3, -4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, sorted(arr))

    def test_empty_array(self):
        arr = []
        n = 0
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [])

    def test_zero_array(self):
        arr = [0, 0, 0, 0, 0]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, arr)

    def test_invalid_n(self):
        arr = [1, 2, 3, 4, 5]
        n = -1
        with self.assertRaises(IndexError):
            re_arrange_array(arr, n)
