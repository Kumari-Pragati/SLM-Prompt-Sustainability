import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_even_sum(self):
        arr = [1, 2, 3, 4]
        n = 4
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_odd_sum(self):
        arr = [1, 2, 3, 5]
        n = 4
        p = 1
        self.assertEqual(check_last(arr, n, p), "ODD")

    def test_zero_sum(self):
        arr = [0, 0, 0, 0]
        n = 4
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_single_element_array(self):
        arr = [1]
        n = 1
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_empty_array(self):
        arr = []
        n = 0
        p = 1
        with self.assertRaises(IndexError):
            check_last(arr, n, p)
