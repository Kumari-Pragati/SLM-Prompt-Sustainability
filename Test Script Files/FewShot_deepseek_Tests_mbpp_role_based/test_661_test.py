import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):
    def test_typical_case(self):
        arr = [3, 6, 9, 12, 15]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 33)

    def test_edge_case_single_element(self):
        arr = [5]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 5)

    def test_boundary_case_two_elements(self):
        arr = [1, 2]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 3)

    def test_boundary_case_three_elements(self):
        arr = [1, 2, 3]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 6)

    def test_invalid_input_negative_numbers(self):
        arr = [-1, -2, -3]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), -1)

    def test_invalid_input_zeroes(self):
        arr = [0, 0, 0]
        n = len(arr)
        self.assertEqual(max_sum_of_three_consecutive(arr, n), 0)

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        self.assertIsNone(max_sum_of_three_consecutive(arr, n))
