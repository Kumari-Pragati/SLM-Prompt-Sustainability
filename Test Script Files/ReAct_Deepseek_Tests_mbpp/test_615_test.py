import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_typical_case(self):
        nums = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        expected_result = [4.0, 5.0, 6.0]
        self.assertEqual(average_tuple(nums), expected_result)

    def test_empty_lists(self):
        nums = ([], [], [])
        expected_result = []
        self.assertEqual(average_tuple(nums), expected_result)

    def test_single_number_lists(self):
        nums = ([1], [2], [3])
        expected_result = [1.0, 2.0, 3.0]
        self.assertEqual(average_tuple(nums), expected_result)

    def test_different_length_lists(self):
        nums = ([1, 2], [3, 4, 5], [6])
        expected_result = [1.5, 4.0, 6.0]
        self.assertEqual(average_tuple(nums), expected_result)

    def test_negative_numbers(self):
        nums = ([-1, -2, -3], [-4, -5, -6], [-7, -8, -9])
        expected_result = [-4.0, -5.0, -6.0]
        self.assertEqual(average_tuple(nums), expected_result)

    def test_zeroes(self):
        nums = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
        expected_result = [0.0, 0.0, 0.0]
        self.assertEqual(average_tuple(nums), expected_result)
