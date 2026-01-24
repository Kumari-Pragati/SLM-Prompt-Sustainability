import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = ['abc', 'def', 'ghi']
        x = 'a'
        self.assertEqual(count_element_in_list(list1, x), 1)

    def test_edge_case_empty_list(self):
        list1 = []
        x = 'a'
        self.assertEqual(count_element_in_list(list1, x), 0)

    def test_boundary_case_single_element_in_list(self):
        list1 = ['abc']
        x = 'a'
        self.assertEqual(count_element_in_list(list1, x), 1)

    def test_boundary_case_single_element_in_list_not_present(self):
        list1 = ['abc']
        x = 'd'
        self.assertEqual(count_element_in_list(list1, x), 0)

    def test_error_handling_invalid_input(self):
        list1 = ['abc', 'def', 'ghi']
        x = 123  # Invalid input, should be a string
        with self.assertRaises(TypeError):
            count_element_in_list(list1, x)
