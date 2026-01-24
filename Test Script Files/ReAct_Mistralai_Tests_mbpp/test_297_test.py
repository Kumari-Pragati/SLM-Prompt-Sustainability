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
        self.assertEqual(flatten_list([1, [2, 3.0], "four", [5, 6, None]]), [1, 2, 3.0, "four", 5, 6, None])

    def test_list_with_empty_nested_list(self):
        self.assertEqual(flatten_list([1, [], 3]), [1, 3])

    def test_list_with_nested_list_of_empty_lists(self):
        self.assertEqual(flatten_list([[[]]]), [])

    def test_list_with_nested_list_of_empty_lists_and_other_elements(self):
        self.assertEqual(flatten_list([1, [[]], 3]), [1, 3])

    def test_list_with_nested_list_of_empty_lists_and_empty_list(self):
        self.assertEqual(flatten_list([[], [[]]]), [])
