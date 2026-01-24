import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 4, 5], 3), 1)
        self.assertEqual(count_element_in_list(["apple", "banana", "cherry"], "apple"), 1)
        self.assertEqual(count_element_in_list([1.1, 2.2, 3.3], 3.3), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_element_in_list([], 1), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_element_in_list([1], 1), 1)

    def test_edge_case_single_element_not_present(self):
        self.assertEqual(count_element_in_list([1], 2), 0)

    def test_boundary_case_negative_numbers(self):
        self.assertEqual(count_element_in_list([-1, -2, -3], -3), 1)

    def test_boundary_case_floats_with_equal_values(self):
        self.assertEqual(count_element_in_list([3.1, 3.2, 3.3], 3.1), 1)

    def test_boundary_case_strings_with_case_sensitivity(self):
        self.assertEqual(count_element_in_list(["Apple", "Banana", "Cherry"], "apple"), 0)
