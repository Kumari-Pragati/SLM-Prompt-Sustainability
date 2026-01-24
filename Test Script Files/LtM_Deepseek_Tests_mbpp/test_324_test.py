import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4)), ((3), (7)))

    def test_empty_input(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_single_element_input(self):
        self.assertEqual(sum_of_alternates((5)), ((5), (0)))

    def test_negative_numbers(self):
        self.assertEqual(sum_of_alternates((-1, 2, -3, 4)), ((-2), (1)))

    def test_large_numbers(self):
        self.assertEqual(sum_of_alternates((1000, 2000, 3000, 4000)), ((6000), (10000)))

    def test_mixed_numbers(self):
        self.assertEqual(sum_of_alternates((1, -2, 3, -4)), ((2), (-2)))
