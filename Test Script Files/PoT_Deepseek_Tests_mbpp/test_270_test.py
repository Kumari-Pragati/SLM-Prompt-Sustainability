import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8, 10], 5), 20)

    def test_edge_case_with_odd_length(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 12)

    def test_boundary_case_with_negative_numbers(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, -6, -8, -10], 5), -20)

    def test_boundary_case_with_zero(self):
        self.assertEqual(sum_even_and_even_index([0, 0, 0, 0, 0], 5), 0)

    def test_corner_case_with_single_even_number(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_corner_case_with_single_odd_number(self):
        self.assertEqual(sum_even_and_even_index([1], 1), 0)

    def test_corner_case_with_all_odd_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7, 9], 5), 0)

    def test_corner_case_with_all_even_numbers(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8, 10], 5), 20)

    def test_invalid_input_with_negative_index(self):
        with self.assertRaises(IndexError):
            sum_even_and_even_index([2, 4, 6, 8, 10], -1)

    def test_invalid_input_with_zero_index(self):
        with self.assertRaises(IndexError):
            sum_even_and_even_index([2, 4, 6, 8, 10], 0)

    def test_invalid_input_with_large_index(self):
        with self.assertRaises(IndexError):
            sum_even_and_even_index([2, 4, 6, 8, 10], 6)
