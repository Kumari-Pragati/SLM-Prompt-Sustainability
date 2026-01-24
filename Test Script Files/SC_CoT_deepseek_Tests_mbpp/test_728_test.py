import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_empty_lists(self):
        self.assertEqual(sum_list([], []), [])

    def test_different_lengths(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5]), [5, 7])

    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, -2, -3], [-4, -5, -6]), [-5, -7, -9])

    def test_large_numbers(self):
        self.assertEqual(sum_list([1000000, 2000000], [3000000, 4000000]), [4000000, 6000000])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_list([1, 2, 3], 'not a list')
