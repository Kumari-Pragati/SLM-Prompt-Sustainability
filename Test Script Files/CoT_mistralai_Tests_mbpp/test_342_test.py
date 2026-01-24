import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(find_minimum_range([]))

    def test_single_element(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))

    def test_multiple_elements_same_value(self):
        self.assertEqual(find_minimum_range([[1, 1], [1, 1]]), (1, 1))

    def test_multiple_elements_different_values(self):
        self.assertEqual(find_minimum_range([[1, 2], [3, 4]]), (1, 2))

    def test_multiple_lists_same_value(self):
        self.assertEqual(find_minimum_range([[1, 1], [1, 1], [1, 1]]), (1, 1))

    def test_multiple_lists_different_values(self):
        self.assertEqual(find_minimum_range([[1, 2], [3, 4], [5, 6]]), (1, 2))

    def test_boundary_empty_list_element(self):
        self.assertIsNone(find_minimum_range([[1]] + [[]]))

    def test_boundary_single_element_list(self):
        self.assertEqual(find_minimum_range([[1]]), (1, 1))

    def test_boundary_multiple_lists_empty_element(self):
        self.assertEqual(find_minimum_range([[1, 2], [], [3, 4]]), (1, 2))

    def test_invalid_input_non_list(self):
        self.assertRaises(TypeError, find_minimum_range, "not a list")
