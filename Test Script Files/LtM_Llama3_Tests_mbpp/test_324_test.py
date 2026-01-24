import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_single_element_input(self):
        self.assertEqual(sum_of_alternates((1,)), ((1), (0)))

    def test_even_length_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4)), ((4), (6)))

    def test_odd_length_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((9), (7)))

    def test_mixed_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, -1, 4, 5)), ((5), (6)))

    def test_negative_input(self):
        self.assertEqual(sum_of_alternates((-1, -2, -3, -4)), ((-6), (-6)))

    def test_max_input(self):
        self.assertEqual(sum_of_alternates((2**31 - 1, 2**31 - 1)), ((2**31 - 1), (2**31 - 1)))

    def test_min_input(self):
        self.assertEqual(sum_of_alternates((-2**31, -2**31)), ((-2**31), (-2**31)))
