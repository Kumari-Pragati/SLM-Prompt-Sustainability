import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(sum_list([]), [])
        self.assertListEqual(sum_list([], [1, 2, 3]), [0, 0, 0])

    def test_single_element_lists(self):
        self.assertListEqual(sum_list([1], []), [1])
        self.assertListEqual(sum_list([], [1]), [1])
        self.assertListEqual(sum_list([1], [2]), [3])

    def test_equal_length_lists(self):
        self.assertListEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_different_length_lists(self):
        self.assertListEqual(sum_list([1, 2, 3], [4, 5]), [5, 7])

    def test_negative_numbers(self):
        self.assertListEqual(sum_list([-1, 2, -3], [4, -5, 6]), [3, -3, 3])

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, sum_list, [1, 2], "not_a_list")
        self.assertRaises(TypeError, sum_list, "not_a_list", [1, 2])
