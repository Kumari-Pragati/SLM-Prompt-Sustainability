import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = 6
        self.assertEqual(sum_even_and_even_index(arr, n), 6)

    def test_all_even(self):
        arr = [2, 4, 6, 8, 10]
        n = 5
        self.assertEqual(sum_even_and_even_index(arr, n), 20)

    def test_all_odd(self):
        arr = [1, 3, 5, 7, 9]
        n = 5
        self.assertEqual(sum_even_and_even_index(arr, n), 0)

    def test_mixed_numbers(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = 6
        self.assertEqual(sum_even_and_even_index(arr, n), 6)

    def test_empty_array(self):
        arr = []
        n = 0
        self.assertEqual(sum_even_and_even_index(arr, n), 0)

    def test_negative_numbers(self):
        arr = [-2, -4, -6, -8, -10]
        n = 5
        self.assertEqual(sum_even_and_even_index(arr, n), -20)

    def test_large_numbers(self):
        arr = [1000000000, 2000000000, 3000000000, 4000000000]
        n = 4
        self.assertEqual(sum_even_and_even_index(arr, n), 6000000000)

    def test_invalid_input(self):
        arr = [1, 2, 3, 4, 5, 6]
        n = -1
        with self.assertRaises(IndexError):
            sum_even_and_even_index(arr, n)
