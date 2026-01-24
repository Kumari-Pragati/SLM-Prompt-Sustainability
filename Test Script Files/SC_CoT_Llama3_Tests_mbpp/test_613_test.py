import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_typical_input(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6), ('c', 9)])

    def test_edge_case_empty_list(self):
        test_list = [('a', [])]
        self.assertEqual(maximum_value(test_list), [('a', None)])

    def test_edge_case_single_element_list(self):
        test_list = [('a', [1])]
        self.assertEqual(maximum_value(test_list), [('a', 1)])

    def test_edge_case_single_element_list_with_none(self):
        test_list = [('a', [1, None])]
        self.assertEqual(maximum_value(test_list), [('a', 1)])

    def test_edge_case_single_element_list_with_none_at_end(self):
        test_list = [('a', [1, None, 2])]
        self.assertEqual(maximum_value(test_list), [('a', 2)])

    def test_edge_case_single_element_list_with_none_at_start(self):
        test_list = [('a', [None, 1, 2])]
        self.assertEqual(maximum_value(test_list), [('a', 2)])

    def test_edge_case_single_element_list_with_none_at_start_and_end(self):
        test_list = [('a', [None, 1, None])]
        self.assertEqual(maximum_value(test_list), [('a', 1)])

    def test_edge_case_multiple_lists(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6), ('c', 9)])

    def test_edge_case_multiple_lists_with_none(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [None, 8, 9])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6), ('c', 9)])

    def test_edge_case_multiple_lists_with_none_at_end(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, None])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6), ('c', 8)])

    def test_edge_case_multiple_lists_with_none_at_start(self):
        test_list = [('a', [None, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, 9])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6), ('c', 9)])

    def test_edge_case_multiple_lists_with_none_at_start_and_end(self):
        test_list = [('a', [None, 2, 3]), ('b', [4, 5, 6]), ('c', [7, 8, None])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6), ('c', 8)])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            maximum_value('test')

    def test_invalid_input_non_dict(self):
        with self.assertRaises(TypeError):
            maximum_value([1, 2, 3])

    def test_invalid_input_non_dict_key(self):
        with self.assertRaises(TypeError):
            maximum_value([('a', [1, 2, 3]), ('b', [4, 5, 6])])
