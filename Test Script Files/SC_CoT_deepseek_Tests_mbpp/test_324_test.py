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
        self.assertEqual(sum_of_alternates((-1, -2, -3, -4, -5)), ((-3), (-1)))

    def test_mixed_numbers(self):
        self.assertEqual(sum_of_alternates((1, -2, 3, -4, 5)), ((3), (6)))

    def test_large_numbers(self):
        self.assertEqual(sum_of_alternates((1000, 2000, 3000, 4000, 5000)), ((9000), (12000)))

    def test_float_numbers(self):
        self.assertEqual(sum_of_alternates((1.5, 2.5, 3.5, 4.5, 5.5)), ((10.5), (12.0)))

    def test_zero_in_tuple(self):
        self.assertEqual(sum_of_alternates((0, 1, 2, 3, 4)), ((3), (9)))
