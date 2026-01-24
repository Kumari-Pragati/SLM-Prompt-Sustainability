import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4]), 6)

    def test_typical_case_with_duplicates(self):
        self.assertEqual(sum_even_odd([1, 2, 2, 3, 4, 4]), 6)

    def test_typical_case_with_negative_numbers(self):
        self.assertEqual(sum_even_odd([-1, -2, 3, 4]), 2)

    def test_typical_case_with_zero(self):
        self.assertEqual(sum_even_odd([0, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(sum_even_odd([]), -1)

    def test_list_with_single_element(self):
        self.assertEqual(sum_even_odd([1]), -1)

    def test_list_with_no_even_no_odd(self):
        self.assertEqual(sum_even_odd([2]), -1)

    def test_list_with_all_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), -1)

    def test_list_with_all_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), -1)
