import unittest
from mbpp_786_code import right_insertion

class TestRightInsertion(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 3), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(right_insertion([], 1), 0)

    def test_edge_case_list_with_one_element(self):
        self.assertEqual(right_insertion([1], 2), 1)

    def test_edge_case_element_greater_than_all(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 6), 5)

    def test_edge_case_element_less_than_all(self):
        self.assertEqual(right_insertion([1, 2, 3, 4, 5], 0), 0)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(right_insertion([1, 2, 2, 3, 4, 5], 2), 2)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            right_insertion(123, 3)

    def test_invalid_input_list_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            right_insertion(['a', 'b', 'c'], 'd')
