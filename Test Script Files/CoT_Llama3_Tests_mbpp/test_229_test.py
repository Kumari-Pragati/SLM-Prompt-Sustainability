import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):
    def test_positive_array(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_negative_array(self):
        arr = [-1, -2, -3, 4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [-3, -2, -1, 4, 5])

    def test_mixed_array(self):
        arr = [1, -2, 3, -4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, -4, 3, -2, 5])

    def test_empty_array(self):
        arr = []
        n = 0
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [])

    def test_zero_array(self):
        arr = [0, 0, 0]
        n = 3
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [0, 0, 0])

    def test_invalid_input(self):
        arr = [1, 2, 3]
        n = -1
        with self.assertRaises(ValueError):
            re_arrange_array(arr, n)
