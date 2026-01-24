import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_re_arrange_typical(self):
        arr = [1, 2, -3, 4, -5, 6]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, 2, -5, 4, -3, 6])

    def test_re_arrange_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_re_arrange_edge_case_negative(self):
        arr = [-1, -2, -3, -4, -5]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [-1, -2, -3, -4, -5])

    def test_re_arrange_edge_case_zero(self):
        arr = [0, 0, 0, 0, 0]
        result = re_arrange(arr, len(arr))
        self.assertEqual(result, [0, 0, 0, 0, 0])

    def test_re_arrange_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            re_arrange(arr,'string')

    def test_re_arrange_invalid_input_negative(self):
        arr = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            re_arrange(arr, -1)
