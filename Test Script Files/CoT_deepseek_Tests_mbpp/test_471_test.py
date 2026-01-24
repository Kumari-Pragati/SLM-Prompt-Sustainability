import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, 20, 30]
        lens = len(arr)
        n = 11
        self.assertEqual(find_remainder(arr, lens, n), 1)

    def test_edge_case_with_zero(self):
        arr = [0, 0, 0]
        lens = len(arr)
        n = 11
        self.assertEqual(find_remainder(arr, lens, n), 0)

    def test_edge_case_with_large_numbers(self):
        arr = [10**10, 20**10, 30**10]
        lens = len(arr)
        n = 11
        self.assertEqual(find_remainder(arr, lens, n), 1)

    def test_invalid_input_negative_n(self):
        arr = [10, 20, 30]
        lens = len(arr)
        n = -11
        with self.assertRaises(Exception):
            find_remainder(arr, lens, n)

    def test_invalid_input_negative_arr_elements(self):
        arr = [-10, -20, -30]
        lens = len(arr)
        n = 11
        self.assertEqual(find_remainder(arr, lens, n), 1)
