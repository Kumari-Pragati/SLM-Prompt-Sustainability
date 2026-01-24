import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(sum_of_alternates(()), (0, 0))

    def test_single_element_tuple(self):
        self.assertEqual(sum_of_alternates((1,)), (1, 0))

    def test_even_length_tuple(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4)), (2, 6))

    def test_odd_length_tuple(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), (3, 9))

    def test_mixed_length_tuple(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5, 6)), (3, 12))

    def test_negative_numbers(self):
        self.assertEqual(sum_of_alternates((-1, 2, -3, 4)), (-2, 5))

    def test_zero(self):
        self.assertEqual(sum_of_alternates((0, 0, 0)), (0, 0))
