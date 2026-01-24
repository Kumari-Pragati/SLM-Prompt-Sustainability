import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(recursive_list_sum([1, 2, 3]), 6)

    def test_nested_list(self):
        self.assertEqual(recursive_list_sum([1, [2, 3], 4]), 10)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(recursive_list_sum([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(recursive_list_sum([1, -1, 2, -2, 3, -3]), 0)

    def test_nested_mixed_numbers(self):
        self.assertEqual(recursive_list_sum([1, [2, -2], -1]), 0)

    def test_nested_empty_list(self):
        self.assertEqual(recursive_list_sum([[], 1]), 1)

    def test_nested_single_element_list(self):
        self.assertEqual(recursive_list_sum([[5], 1]), 6)
