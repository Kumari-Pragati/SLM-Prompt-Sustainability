import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_sum_even_and_even_index(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)
        self.assertEqual(sum_even_and_even_index([10, 20, 30, 40, 50, 60], 6), 150)
        self.assertEqual(sum_even_and_even_index([1, 3, 5, 7, 9, 11], 6), 0)
        self.assertEqual(sum_even_and_even_index([2, 4, 6, 8, 10, 12], 6, 6), 30)
        self.assertEqual(sum_even_and_even_index([], 0), 0)
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 0), 0)

    def test_sum_even_and_even_index_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_even_and_even_index([1, 2, 3, 4, 5, 6], 'a')
        with self.assertRaises(TypeError):
            sum_even_and_even_index([1, 2, 3, 4, 5, 6], -1)
