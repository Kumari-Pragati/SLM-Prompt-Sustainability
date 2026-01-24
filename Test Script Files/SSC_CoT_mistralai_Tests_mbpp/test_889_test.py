import unittest
from mbpp_889_code import deepcopy
from 889_code import reverse_list_lists

class TestReverseListLists(unittest.TestCase):

    def test_normal_case(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [3, 2, 1],
            [6, 5, 4],
            [9, 8, 7]
        ]
        self.assertEqual(reverse_list_lists(data), expected)

    def test_empty_list(self):
        data = []
        self.assertEqual(reverse_list_lists(data), [])

    def test_single_element_list(self):
        data = [
            [1]
        ]
        expected = [
            [1]
        ]
        self.assertEqual(reverse_list_lists(data), expected)

    def test_negative_numbers(self):
        data = [
            [-1, 0, 1],
            [-2, -3, -4]
        ]
        expected = [
            [1, 0, -1],
            [-4, -3, -2]
        ]
        self.assertEqual(reverse_list_lists(data), expected)

    def test_mixed_types(self):
        data = [
            [1, 2, "a"],
            ["b", 3, 4]
        ]
        expected = [
            ["a", 2, 1],
            ["4", 3, "b"]
        ]
        self.assertEqual(reverse_list_lists(data), expected)

    def test_invalid_input(self):
        data = [1, 2, 3, "invalid"]
        with self.assertRaises(TypeError):
            reverse_list_lists(data)
