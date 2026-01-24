import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_single_element(self):
        for num in range(-10, 11):
            self.assertEqual(max_sub_array_sum([num], 1), num)

    def test_positive_numbers(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for size in range(1, len(data)+1):
            self.assertEqual(max_sub_array_sum(data, size), sum(data))

    def test_negative_numbers(self):
        data = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        for size in range(1, len(data)+1):
            self.assertEqual(max_sub_array_sum(data, size), max(data))

    def test_mixed_numbers(self):
        data = [1, -2, 3, -4, 5, -6, 7, -8, 9]
        for size in range(1, len(data)+1):
            self.assertGreaterEqual(max_sub_array_sum(data, size), sum(data[::size]) if size <= len(data) else 0)

    def test_zero_size(self):
        self.assertEqual(max_sub_array_sum([0], 0), 0)

    def test_negative_size(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3], -1), 0)
        self.assertEqual(max_sub_array_sum([1, 2, 3], -len(data)), 0)
