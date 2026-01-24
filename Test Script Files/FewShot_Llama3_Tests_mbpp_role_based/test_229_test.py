import unittest
from mbpp_229_code import re_arrange_array

class TestReArrangeArray(unittest.TestCase):
    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [1, -2, 3, -4, 5])

    def test_zero(self):
        arr = [0, 0, 0, 0, 0]
        n = 5
        result = re_arrange_array(arr, n)
        self.assertEqual(result, [0, 0, 0, 0, 0])

    def test_invalid_input_type(self):
        arr = "Invalid input"
        n = 5
        with self.assertRaises(TypeError):
            re_arrange_array(arr, n)

    def test_invalid_input_value(self):
        arr = [1, 2, 3]
        n = "Invalid input"
        with self.assertRaises(TypeError):
            re_arrange_array(arr, n)
