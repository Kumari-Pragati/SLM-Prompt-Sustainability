import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_level_list(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_nested_list(self):
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_nested_list_with_empty_sublist(self):
        self.assertEqual(flatten_list([1, [2, []], 3]), [1, 2, 3])

    def test_nested_list_with_multiple_levels(self):
        self.assertEqual(flatten_list([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])

    def test_nested_list_with_non_list_elements(self):
        self.assertEqual(flatten_list([1, [2, '3'], 4]), [1, 2, '3', 4])

    def test_list_with_non_list_elements(self):
        self.assertEqual(flatten_list([1, '2', 3]), [1, '2', 3])

    def test_list_with_none_elements(self):
        self.assertEqual(flatten_list([1, None, 3]), [1, None, 3])

    def test_list_with_mixed_types(self):
        self.assertEqual(flatten_list([1, '2', [3, None]]), [1, '2', 3, None])
