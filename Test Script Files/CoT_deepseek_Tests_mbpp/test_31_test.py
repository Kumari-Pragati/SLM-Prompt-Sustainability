import unittest
from mbpp_31_code import func

class TestFunc(unittest.TestCase):

    def test_typical_case(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 2
        expected_output = [3, 4]
        self.assertEqual(func(nums, k), expected_output)

    def test_single_number(self):
        nums = [[1], [2], [3]]
        k = 1
        expected_output = [1]
        self.assertEqual(func(nums, k), expected_output)

    def test_empty_list(self):
        nums = []
        k = 1
        expected_output = []
        self.assertEqual(func(nums, k), expected_output)

    def test_large_k(self):
        nums = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        k = 10
        expected_output = [5]
        self.assertEqual(func(nums, k), expected_output)

    def test_negative_numbers(self):
        nums = [[-1, -2, -3], [-2, -3, -4], [-3, -4, -5]]
        k = 2
        expected_output = [-3, -4]
        self.assertEqual(func(nums, k), expected_output)

    def test_zero(self):
        nums = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
        k = 1
        expected_output = [2]
        self.assertEqual(func(nums, k), expected_output)
