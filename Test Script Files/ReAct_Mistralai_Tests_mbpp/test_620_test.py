import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_subset([], 0), 0)

    def test_single_element(self):
        for num in range(1, 10):
            self.assertEqual(largest_subset([num], 1), 1)

    def test_two_elements(self):
        for a, b in [(2, 3), (3, 2), (2, 4), (4, 2), (5, 2), (2, 5), (3, 4), (4, 3)]:
            self.assertEqual(largest_subset([a, b], 2), max([1, 2]))

    def test_three_elements(self):
        for a, b, c in [(2, 3, 4), (3, 2, 4), (2, 3, 5), (3, 2, 5), (2, 4, 3), (4, 2, 3), (2, 4, 5), (4, 2, 5), (3, 4, 2), (4, 3, 2), (5, 2, 3), (5, 3, 2)]:
            self.assertEqual(largest_subset([a, b, c], 3), max([1, 2, 3]))

    def test_large_list(self):
        data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(largest_subset(data, len(data)), max(data))

    def test_non_integer_input(self):
        self.assertRaises(TypeError, largest_subset, [1, 2, 3], 'a')

    def test_negative_numbers(self):
        data = [-2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]
        self.assertEqual(largest_subset(data, len(data)), max(data))

    def test_fractions(self):
        data = [1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10, 1/11, 1/12, 1/13, 1/14, 1/15, 1/16, 1/17, 1/18, 1/19, 1/20]
        self.assertEqual(largest_subset(data, len(data)), max(data))
