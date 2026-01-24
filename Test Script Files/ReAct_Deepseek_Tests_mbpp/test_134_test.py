import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_typical_case_even(self):
        arr = [1, 2, 3, 4]
        n = len(arr)
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_typical_case_odd(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        p = 1
        self.assertEqual(check_last(arr, n, p), "ODD")

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        p = 1
        self.assertEqual(check_last(arr, n, p), "ODD")

    def test_edge_case_empty_array(self):
        arr = []
        n = 0
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_error_case_negative_elements(self):
        arr = [1, -2, 3, 4]
        n = len(arr)
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_error_case_non_integer_elements(self):
        arr = [1, 2, 3, '4']
        n = len(arr)
        p = 1
        self.assertRaises(TypeError, check_last, arr, n, p)
