import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15)

    def test_typical_case_with_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], 5]), 15)

    def test_typical_case_with_nested_lists_and_mixed_types(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, '4'], 5]), 12)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([5]), 5)

    def test_list_with_negative_numbers(self):
        self.assertEqual(recursive_list_sum([1, -2, 3, -4, 5]), 5)

    def test_list_with_zero(self):
        self.assertEqual(recursive_list_sum([0, 1, 2, 3, 4]), 10)

    def test_list_with_strings(self):
        with self.assertRaises(TypeError):
            recursive_list_sum(['1', '2', '3', '4', '5'])

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            recursive_list_sum([1, '2', 3, '4', 5])
