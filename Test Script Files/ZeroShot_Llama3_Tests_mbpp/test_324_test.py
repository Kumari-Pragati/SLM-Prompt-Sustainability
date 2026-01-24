import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_sum_of_alternates(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((1+3+5), (2+4)))
        self.assertEqual(sum_of_alternates((-1, -2, -3, -4, -5)), ((-1-3-5), (-2-4)))
        self.assertEqual(sum_of_alternates((1, 1, 1, 1, 1)), ((1+1+1), (1+1+1)))
        self.assertEqual(sum_of_alternates((0, 0, 0, 0, 0)), ((0), (0)))
        self.assertEqual(sum_of_alternates((-1, 0, 1, 0, -1)), ((-1+1), (0+0-1)))
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5, 6)), ((1+3+5+6), (2+4)))

    def test_sum_of_alternates_empty(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_sum_of_alternates_single(self):
        self.assertEqual(sum_of_alternates((1)), ((1), (0)))

    def test_sum_of_alternates_two(self):
        self.assertEqual(sum_of_alternates((1, 2)), ((1), (2)))
