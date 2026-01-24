import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_odd([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_odd([1]), 1)

    def test_edge_case_single_even_element(self):
        self.assertEqual(count_odd([2]), 0)

    def test_edge_case_single_odd_element(self):
        self.assertEqual(count_odd([1]), 1)

    def test_edge_case_single_zero(self):
        self.assertEqual(count_odd([0]), 0)

    def test_edge_case_single_negative(self):
        self.assertEqual(count_odd([-1]), 1)

    def test_edge_case_multiple_odd_and_even(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6]), 3)

    def test_edge_case_multiple_consecutive_odd(self):
        self.assertEqual(count_odd([1, 3, 5, 7, 9]), 5)

    def test_edge_case_multiple_consecutive_even(self):
        self.assertEqual(count_odd([2, 4, 6, 8, 10]), 0)

    def test_edge_case_multiple_consecutive_mixed(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(count_odd([-1, -2, -3, -4, -5]), 3)

    def test_edge_case_mixed_positive_and_negative(self):
        self.assertEqual(count_odd([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]), 5)

    def test_edge_case_mixed_positive_and_negative_with_zero(self):
        self.assertEqual(count_odd([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 0]), 5)

    def test_edge_case_mixed_positive_and_negative_with_zero_and_even(self):
        self.assertEqual(count_odd([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 0, 6]), 5)

    def test_edge_case_mixed_positive_and_negative_with_zero_and_even_and_negative(self):
        self.assertEqual(count_odd([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 0, 6, -7]), 5)

    def test_edge_case_mixed_positive_and_negative_with_zero_and_even_and_negative_and_positive(self):
        self.assertEqual(count_odd([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 0, 6, -7, 8]), 6)

    def test_edge_case_mixed_positive_and_negative_with_zero_and_even_and_negative_and_positive_and_negative(self):
        self.assertEqual(count_odd([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, 0, 6, -7, 8, -9]), 6)
