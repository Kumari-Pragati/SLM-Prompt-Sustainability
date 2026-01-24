import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):
    def test_positive_array(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_negative_array(self):
        arr = [-1, -2, -3, -4, -5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [-5, -4, -3, -2, -1])

    def test_mixed_array(self):
        arr = [1, -2, 3, -4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, -2, 3, -4, 5])

    def test_empty_array(self):
        arr = []
        n = 0
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [])

    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 4, 5]
        n = 7
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, 2, 2, 3, 4, 4, 5])

    def test_invalid_input_type(self):
        arr = [1, 2, 3, 4, 5]
        n = 'five'
        with self.assertRaises(TypeError):
            re_arrange_array(arr, n)

    def test_invalid_input_value(self):
        arr = [1, 2, 3, 4, 5]
        n = -5
        with self.assertRaises(ValueError):
            re_arrange_array(arr, n)
