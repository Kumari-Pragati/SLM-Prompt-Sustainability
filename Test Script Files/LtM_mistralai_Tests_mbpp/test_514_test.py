import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)
        self.assertEqual(sum_elements((0, 0, 0)), 0)
        self.assertEqual(sum_elements((-1, -2, -3)), -6)

    def test_single_input(self):
        self.assertEqual(sum_elements((1)), 1)
        self.assertEqual(sum_elements((-1)), -1)

    def test_empty_input(self):
        self.assertEqual(sum_elements(()), 0)

    def test_large_input(self):
        large_list = [i for i in range(1000)]
        self.assertEqual(sum_elements(tuple(large_list)), sum(large_list))

    def test_negative_numbers(self):
        self.assertEqual(sum_elements((1, -1, 2, -2, 3, -3)), 0)

    def test_mixed_numbers(self):
        self.assertEqual(sum_elements((1, -2, 3, -4, 5, -6)), 1)
