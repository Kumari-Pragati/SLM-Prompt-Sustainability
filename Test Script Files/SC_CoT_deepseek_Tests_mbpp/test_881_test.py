import unittest
from mbpp_881_code import sum_even_odd

class TestSumEvenOdd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4]), 6)

    def test_empty_list(self):
        self.assertEqual(sum_even_odd([]), -2)

    def test_all_even(self):
        self.assertEqual(sum_even_odd([2, 4, 6]), -1)

    def test_all_odd(self):
        self.assertEqual(sum_even_odd([1, 3, 5]), -1)

    def test_single_element(self):
        self.assertEqual(sum_even_odd([1]), -1)

    def test_negative_numbers(self):
        self.assertEqual(sum_even_odd([-1, -2, -3, -4]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(sum_even_odd([1, 2, 3, 4, 5]), 6)

    def test_large_numbers(self):
        self.assertEqual(sum_even_odd([1000000000, 2000000000, 3000000000]), -1)

    def test_duplicates(self):
        self.assertEqual(sum_even_odd([2, 2, 3, 4]), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_even_odd('not a list')
