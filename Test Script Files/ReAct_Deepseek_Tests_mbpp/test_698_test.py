import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'b': 2, 'a': 1, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_edge_case_single_item(self):
        test_dict = {'a': 1}
        expected_output = {'a': 1}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_edge_case_empty_dict(self):
        test_dict = {}
        expected_output = {}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_edge_case_same_values(self):
        test_dict = {'b': 2, 'a': 2, 'c': 2}
        expected_output = {'a': 2, 'b': 2, 'c': 2}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_error_case_non_dict_input(self):
        with self.assertRaises(TypeError):
            sort_dict_item('not a dict')
