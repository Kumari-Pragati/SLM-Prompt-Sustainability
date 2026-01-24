import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):
    def test_typical_use_case(self):
        test_dict = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_edge_case_with_same_values(self):
        test_dict = {'b': 2, 'a': 2, 'd': 4, 'c': 4}
        expected_output = {'a': 2, 'b': 2, 'c': 4, 'd': 4}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_boundary_case_with_negative_values(self):
        test_dict = {'b': -2, 'a': -1, 'd': -4, 'c': -3}
        expected_output = {'a': -1, 'b': -2, 'c': -3, 'd': -4}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_dict_item(123)
