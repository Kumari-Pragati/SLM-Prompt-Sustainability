import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'b': 2, 'a': 1, 'c': 3}
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_edge_case(self):
        test_dict = {'b': 2, 'a': 1, 'c': 3, 'd': 4}
        expected_output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_corner_case(self):
        test_dict = {'10': 10, '2': 2, '1': 1}
        expected_output = {'1': 1, '2': 2, '10': 10}
        self.assertEqual(sort_dict_item(test_dict), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_dict_item(123)
