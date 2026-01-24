import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((9), (14)))

    def test_empty_tuple(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_single_element_tuple(self):
        self.assertEqual(sum_of_alternates((10,)), ((10), (0)))

    def test_negative_numbers(self):
        self.assertEqual(sum_of_alternates((-1, 2, -3, 4, -5)), ((-2), (6)))

    def test_zero_numbers(self):
        self.assertEqual(sum_of_alternates((0, 0, 0, 0)), ((0), (0)))

    def test_large_numbers(self):
        self.assertEqual(sum_of_alternates((1000000, 2000000, 3000000)), ((6000000), (0)))
