import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):
    def test_typical_case(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6), ('c', 9)])

    def test_edge_case_empty_list(self):
        test_list = []
        self.assertEqual(maximum_value(test_list), [])

    def test_edge_case_single_element_list(self):
        test_list = [('a', [1])]
        self.assertEqual(maximum_value(test_list), [('a', 1)])

    def test_edge_case_single_element_list_with_duplicates(self):
        test_list = [('a', [1, 1, 1])]
        self.assertEqual(maximum_value(test_list), [('a', 1)])

    def test_invalid_input_non_list(self):
        test_list = 'not a list'
        with self.assertRaises(TypeError):
            maximum_value(test_list)

    def test_invalid_input_non_list_of_lists(self):
        test_list = [('a', 1), ('b', 2)]
        with self.assertRaises(TypeError):
            maximum_value(test_list)
