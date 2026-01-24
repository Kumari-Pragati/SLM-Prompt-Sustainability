import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_empty_lists(self):
        self.assertListEqual(add_list([]), [])
        self.assertListEqual(add_list([], [1]), [1])
        self.assertListEqual(add_list([], [1, 2, 3]), [1, 2, 3])
        self.assertListEqual(add_list([1], []), [1])

    def test_single_element_lists(self):
        self.assertListEqual(add_list([1], [2]), [3])
        self.assertListEqual(add_list([2], [1]), [3])

    def test_lists_with_same_length(self):
        self.assertListEqual(add_list([1, 2], [3, 4]), [4, 6])
        self.assertListEqual(add_list([3, 4], [1, 2]), [4, 6])

    def test_lists_with_different_lengths(self):
        self.assertListEqual(add_list([1, 2], [3]), [4, 2])
        self.assertListEqual(add_list([3], [1, 2]), [4, 2])

    def test_lists_with_negative_numbers(self):
        self.assertListEqual(add_list([1, -2], [3, -4]), [4, -2])
        self.assertListEqual(add_list([3, -4], [1, -2]), [4, -2])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, add_list, [1], "not_a_number")
        self.assertRaises(TypeError, add_list, "not_a_number", [1])
