import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_edge_case_n_zero(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 0), 0)

    def test_edge_case_n_equal_to_length(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_edge_case_n_greater_than_length(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 7), 12)

    def test_special_case_no_even_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7, 9, 11], 6), 0)

    def test_special_case_all_even_numbers(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8, 10, 12], 6), 30)

    def test_invalid_input_non_integer_n(self):
        with self.assertRaises(TypeError):
            sum_even_and_even_index([1, 2, 3, 4, 5, 6], 'a')

    def test_invalid_input_non_list_input(self):
        with self.assertRaises(TypeError):
            sum_even_and_even_index('hello', 6)
