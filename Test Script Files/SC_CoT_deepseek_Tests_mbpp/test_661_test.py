import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):
    
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 15)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 1)

    def test_edge_case_two_elements(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 3)

    def test_edge_case_three_elements(self):
        arr = [1, 2, 3]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 6)

    def test_corner_case_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), -6)

    def test_corner_case_all_positive(self):
        arr = [10, 20, 30, 40, 50]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 120)

    def test_corner_case_all_negative(self):
        arr = [-10, -20, -30, -40, -50]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), -60)

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        with self.assertRaises(IndexError):
            max_sum_of_three_consecutive(arr, n)

    def test_invalid_input_negative_length(self):
        arr = [1, 2, 3]
        n = -1
        with self.assertRaises(IndexError):
            max_sum_of_three_consecutive(arr, n)
