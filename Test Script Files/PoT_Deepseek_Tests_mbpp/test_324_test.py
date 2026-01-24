import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), (9, 6))

    def test_empty_tuple(self):
        self.assertEqual(sum_of_alternates(()), (0, 0))

    def test_single_element_tuple(self):
        self.assertEqual(sum_of_alternates((10,)), (10, 0))

    def test_negative_numbers(self):
        self.assertEqual(sum_of_alternates((-1, -2, -3, -4, -5)), (-9, -6))

    def test_mixed_numbers(self):
        self.assertEqual(sum_of_alternates((1, -2, 3, -4, 5)), (9, -6))

    def test_large_numbers(self):
        self.assertEqual(sum_of_alternates((1000, 2000, 3000, 4000, 5000)), (15000, 10000))
