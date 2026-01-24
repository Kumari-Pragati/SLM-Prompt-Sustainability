import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(recursive_list_sum([1, -2, 3]), 4)

    def test_empty_nested_list(self):
        self.assertEqual(recursive_list_sum([1, [], 3]), 6)

    def test_only_nested_list(self):
        self.assertEqual(recursive_list_sum([[1, 2, 3]]), 6)

    def test_non_list_input(self):
        self.assertRaises(TypeError, recursive_list_sum, "not a list")
