import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(flatten_list([1]), [1])

    def test_list_with_single_nested_list(self):
        self.assertEqual(flatten_list([1, [2]]), [1, 2])

    def test_list_with_multiple_nested_lists(self):
        self.assertEqual(flatten_list([1, [2, [3]], 4]), [1, 2, 3, 4])

    def test_list_with_only_nested_lists(self):
        self.assertEqual(flatten_list([[1], [2], [3]]), [1, 2, 3])

    def test_list_with_mixed_types(self):
        self.assertEqual(flatten_list([1, [2, 3], "four", [5, 6, 7]]), [1, 2, 3, "four", 5, 6, 7])

    def test_list_with_empty_nested_lists(self):
        self.assertEqual(flatten_list([1, [], [3], [], 5]), [1, 3, 5])

    def test_list_with_nested_lists_of_different_lengths(self):
        self.assertEqual(flatten_list([[1], [2, 3], [], [4, 5]]), [1, 2, 3, 4, 5])

    def test_list_with_nested_lists_of_different_types(self):
        self.assertEqual(flatten_list([[1], [2, 3], [], [4, "five"]]), [1, 2, 3, 4, "five"])

    def test_list_with_nested_lists_of_different_types_and_lengths(self):
        self.assertEqual(flatten_list([[1], [2, 3], [], [4, "five", 6]]), [1, 2, 3, 4, "five", 6])
