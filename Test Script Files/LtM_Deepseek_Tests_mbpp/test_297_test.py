import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(flatten_list([1, 2, 3]), [1, 2, 3])

    def test_nested_list(self):
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_nested_list_with_empty_list(self):
        self.assertEqual(flatten_list([1, [], 2]), [1, 2])

    def test_nested_list_with_empty_list_at_start(self):
        self.assertEqual(flatten_list([[], 1, 2]), [1, 2])

    def test_nested_list_with_empty_list_in_nested_list(self):
        self.assertEqual(flatten_list([1, [2, []], 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_list_with_single_element(self):
        self.assertEqual(flatten_list([5]), [5])

    def test_list_with_single_nested_list(self):
        self.assertEqual(flatten_list([[7]]), [7])

    def test_list_with_single_nested_list_with_elements(self):
        self.assertEqual(flatten_list([[8, 9]]), [8, 9])
