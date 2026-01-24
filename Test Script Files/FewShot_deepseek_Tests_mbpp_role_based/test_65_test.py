import unittest
from mbpp_65_code import recursive_list_sum

class TestRecursiveListSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(recursive_list_sum([1, 2, 3, 4, 5]), 15)

    def test_typical_use_case_with_nested_lists(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], 5]), 15)

    def test_typical_use_case_with_nested_lists_and_zero(self):
        self.assertEqual(recursive_list_sum([0, 2, [3, 4], 5]), 11)

    def test_boundary_condition_with_empty_list(self):
        self.assertEqual(recursive_list_sum([]), 0)

    def test_boundary_condition_with_single_element_list(self):
        self.assertEqual(recursive_list_sum([5]), 5)

    def test_boundary_condition_with_nested_empty_list(self):
        self.assertEqual(recursive_list_sum([[],[],[],[]]), 0)

    def test_boundary_condition_with_nested_single_element_list(self):
        self.assertEqual(recursive_list_sum([[5],[5],[5],[5]]), 20)

    def test_error_handling_with_non_list_input(self):
        with self.assertRaises(TypeError):
            recursive_list_sum("1, 2, 3, 4, 5")
