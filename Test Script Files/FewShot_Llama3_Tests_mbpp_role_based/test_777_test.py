import unittest
from mbpp_777_code import find_Sum

class TestFindSum(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = 3
        self.assertEqual(find_Sum(arr, n), 9)

    def test_edge_case_n_is_1(self):
        arr = [1, 2, 3, 4, 5]
        n = 1
        self.assertEqual(find_Sum(arr, n), 1)

    def test_edge_case_n_is_length_of_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(find_Sum(arr, n), 15)

    def test_array_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 4, 5]
        n = 3
        self.assertEqual(find_Sum(arr, n), 9)

    def test_array_with_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        n = 2
        self.assertEqual(find_Sum(arr, n), -3)

    def test_invalid_input_type(self):
        arr = [1, 2, 3, 4, 5]
        n = 'a'
        with self.assertRaises(TypeError):
            find_Sum(arr, n)
