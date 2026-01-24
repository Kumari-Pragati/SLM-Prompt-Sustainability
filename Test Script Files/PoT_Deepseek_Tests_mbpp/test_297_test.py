import unittest
from mbpp_297_code import flatten_list

class TestFlattenList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(flatten_list([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])

    def test_empty_list(self):
        self.assertEqual(flatten_list([]), [])

    def test_single_element(self):
        self.assertEqual(flatten_list([7]), [7])

    def test_nested_empty_list(self):
        self.assertEqual(flatten_list([[], []]), [])

    def test_nested_with_empty_list(self):
        self.assertEqual(flatten_list([1, [], 2]), [1, 2])

    def test_nested_with_single_element(self):
        self.assertEqual(flatten_list([1, [2], 3]), [1, 2, 3])

    def test_nested_with_single_element_and_empty_list(self):
        self.assertEqual(flatten_list([1, [], [2], 3]), [1, 2, 3])

    def test_nested_with_single_element_and_empty_list_and_single_element(self):
        self.assertEqual(flatten_list([1, [], [2], 3, [], 4]), [1, 2, 3, 4])

    def test_nested_with_single_element_and_empty_list_and_single_element_and_empty_list(self):
        self.assertEqual(flatten_list([1, [], [2], 3, [], 4, []]), [1, 2, 3, 4])

    def test_nested_with_single_element_and_empty_list_and_single_element_and_empty_list_and_single_element(self):
        self.assertEqual(flatten_list([1, [], [2], 3, [], 4, [], 5]), [1, 2, 3, 4, 5])
