import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(flatten_list([1]), [1])

    def test_list_with_multiple_elements(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_list_with_nested_lists(self):
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_list_with_only_nested_lists(self):
        self.assertEqual(flatten_list([[1], [2, 3], [4]]), [1, 2, 3, 4])

    def test_list_with_mixed_types(self):
        self.assertEqual(flatten_list([1, 'str', [2, 3], 4.5]), [1, 'str', 2, 3, 4.5])

    def test_list_with_empty_nested_lists(self):
        self.assertEqual(flatten_list([1, [], [2, 3], [], 4]), [1, 2, 3, 4])

    def test_list_with_nested_lists_and_empty_elements(self):
        self.assertEqual(flatten_list([[1], [], [2, 3], [], [4, []]]), [1, 2, 3, 4])
