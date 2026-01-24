import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_odd_count_even(self):
        arr = [1, 3, 5, 7]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_odd_count_odd(self):
        arr = [1, 3, 5, 7, 9]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 1)

    def test_boundary_case_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(min_Num(arr, n), 2)

    def test_boundary_case_single_even_number(self):
        arr = [2]
        n = 1
        self.assertEqual(min_Num(arr, n), 2)

    def test_boundary_case_single_odd_number(self):
        arr = [1]
        n = 1
        self.assertEqual(min_Num(arr, n), 1)

    def test_edge_case_all_even_numbers(self):
        arr = [2, 4, 6, 8]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 2)

    def test_edge_case_all_odd_numbers(self):
        arr = [1, 3, 5, 7]
        n = len(arr)
        self.assertEqual(min_Num(arr, n), 1)

    def test_invalid_input_negative_numbers(self):
        arr = [-1, -3, -5, -7]
        n = len(arr)
        with self.assertRaises(Exception):
            min_Num(arr, n)

    def test_invalid_input_non_integer_array(self):
        arr = [1, 2, 3, 'a']
        n = len(arr)
        with self.assertRaises(Exception):
            min_Num(arr, n)
