import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15)

    def test_typical_case_with_nested_list(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], 5]), 15)

    def test_typical_case_with_nested_list_and_zero(self):
        self.assertEqual(recursive_list_sum([0, 1, 2, [3, 4], 5]), 14)

    def test_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(recursive_list_sum([1]), 1)

    def test_single_element_nested_list(self):
        self.assertEqual(recursive_list_sum([[1]]), 1)

    def test_negative_numbers(self):
        self.assertEqual(recursive_list_sum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(recursive_list_sum([-1, 2, -3, 4, -5]), -3)

    def test_float_numbers(self):
        self.assertEqual(recursive_list_sum([1.5, 2.5]), 4.0)

    def test_nested_list_with_float_numbers(self):
        self.assertEqual(recursive_list_sum([1.5, 2.5, [3.5, 4.5]]), 13.0)

    def test_nested_list_with_mixed_numbers(self):
        self.assertEqual(recursive_list_sum([1, 2, [3.5, 4.5], -5]), 3.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            recursive_list_sum(123)

        with self.assertRaises(TypeError):
            recursive_list_sum('123')

        with self.assertRaises(TypeError):
            recursive_list_sum(None)

        with self.assertRaises(TypeError):
            recursive_list_sum(True)

        with self.assertRaises(TypeError):
            recursive_list_sum(False)
