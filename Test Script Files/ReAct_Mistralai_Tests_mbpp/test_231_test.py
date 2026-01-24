import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum([[1]], 1), 1)

    def test_two_elements(self):
        self.assertEqual(max_sum([[1, 2], [3, 4]], 2), max(4, 7))

    def test_three_elements(self):
        self.assertEqual(max_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), max(15, 20, 24))

    def test_large_list(self):
        large_list = [[i*j for j in range(1, 11)] for i in range(1, 11)]
        self.assertEqual(max_sum(large_list, len(large_list)), max(sum(row) for row in large_list[-1]))

    def test_negative_numbers(self):
        self.assertEqual(max_sum([[-1, 2, -3], [4, -5, 6], [-7, 8, 9]], 3), max(1, -2, 11))

    def test_zero_numbers(self):
        self.assertEqual(max_sum([[0, 2, 0], [4, 0, 6], [0, 8, 0]], 3), max(0, 2, 8))
