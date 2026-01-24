import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8], 4), 12)

    def test_with_odd_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7], 4), 0)

    def test_with_mixed_numbers(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6, 7, 8], 8), 12)

    def test_with_negative_numbers(self):
        self.assertEqual(sum_even_and_even_index([-2, -4, -6, -8], 4), -12)

    def test_with_zero(self):
        self.assertEqual(sum_even_and_even_index([0, 2, 4, 6], 4), 6)

    def test_with_single_element(self):
        self.assertEqual(sum_even_and_even_index([2], 1), 2)

    def test_with_empty_list(self):
        self.assertEqual(sum_even_and_even_index([], 0), 0)

    def test_with_large_numbers(self):
        self.assertEqual(sum_even_and_even_index([1000000000, 2000000000, 3000000000, 4000000000], 4), 6000000000)

    def test_with_float_numbers(self):
        self.assertEqual(sum_even_and_even_index([1.5, 3.5, 5.5, 7.5], 4), 0.0)

    def test_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            sum_even_and_even_index([1, 2.5, 3, 4.5], 4)
