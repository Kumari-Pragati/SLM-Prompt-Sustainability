import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_typical_case(self):
        nums = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
        expected_output = [4.0, 5.0, 6.0]
        self.assertEqual(average_tuple(nums), expected_output)

    def test_edge_case_single_number(self):
        nums = ([1], [2], [3])
        expected_output = [2.0]
        self.assertEqual(average_tuple(nums), expected_output)

    def test_boundary_case_empty_lists(self):
        nums = ([], [], [])
        expected_output = []
        self.assertEqual(average_tuple(nums), expected_output)

    def test_special_case_negative_numbers(self):
        nums = ([-1, -2, -3], [-4, -5, -6], [-7, -8, -9])
        expected_output = [-4.0, -5.0, -6.0]
        self.assertEqual(average_tuple(nums), expected_output)

    def test_invalid_input_different_length_lists(self):
        nums = ([1, 2, 3], [4, 5], [6])
        with self.assertRaises(ValueError):
            average_tuple(nums)
