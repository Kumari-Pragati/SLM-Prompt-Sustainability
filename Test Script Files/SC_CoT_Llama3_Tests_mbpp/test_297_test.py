import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(flatten_list([1]), [1])

    def test_nested_list(self):
        self.assertEqual(flatten_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_multiple_nested_list(self):
        self.assertEqual(flatten_list([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])

    def test_list_with_non_list_elements(self):
        self.assertEqual(flatten_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_list_with_mixed_elements(self):
        self.assertEqual(flatten_list([1, 2, [3, 4], 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_list_with_empty_list(self):
        self.assertEqual(flatten_list([1, [2, 3], [], 4]), [1, 2, 3, 4])

    def test_list_with_empty_list_at_end(self):
        self.assertEqual(flatten_list([1, [2, 3], 4, []]), [1, 2, 3, 4])

    def test_list_with_empty_list_at_start(self):
        self.assertEqual(flatten_list([[], 1, [2, 3], 4]), [1, 2, 3, 4])

    def test_list_with_empty_list_in_middle(self):
        self.assertEqual(flatten_list([1, [], 2, [3, 4], 5]), [1, 2, 3, 4, 5])
