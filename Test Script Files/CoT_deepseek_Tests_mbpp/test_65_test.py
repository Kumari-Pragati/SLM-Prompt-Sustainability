import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15)

    def test_typical_case_with_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], 5]), 15)

    def test_typical_case_with_nested_and_mixed_lists(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, [4, 5]], 6]), 21)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(recursive_list_sum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers_and_lists(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], -5]), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            recursive_list_sum(123)

        with self.assertRaises(TypeError):
            recursive_list_sum('not a list')
