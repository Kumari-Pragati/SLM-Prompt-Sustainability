import unittest
from mbpp_57_code import find_Max_Num

class TestFindMaxNum(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [3, 6, 9, 1]
        n = 4
        self.assertEqual(find_Max_Num(arr, n), 9631)

    def test_edge_case_single_digit(self):
        arr = [1]
        n = 1
        self.assertEqual(find_Max_Num(arr, n), 1)

    def test_edge_case_zero(self):
        arr = [0, 0, 0]
        n = 3
        self.assertEqual(find_Max_Num(arr, n), 0)

    def test_edge_case_negative_numbers(self):
        arr = [-1, -2, -3]
        n = 3
        self.assertEqual(find_Max_Num(arr, n), -321)

    def test_edge_case_empty_array(self):
        arr = []
        n = 0
        with self.assertRaises(IndexError):
            find_Max_Num(arr, n)

    def test_edge_case_invalid_input_type(self):
        arr = [1, 2, 3]
        n = 'a'
        with self.assertRaises(TypeError):
            find_Max_Num(arr, n)
