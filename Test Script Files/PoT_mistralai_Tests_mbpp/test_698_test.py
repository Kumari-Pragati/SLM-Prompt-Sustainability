import unittest
from mbpp_698_code import MutableMapping

class TestSortDictItem(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}
        expected_result = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_zero(self):
        test_dict = {(0, 0): 'a', (1, 1): 'b', (2, 2): 'c'}
        expected_result = {(0, 0): 'a', (1, 1): 'b', (2, 2): 'c'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_negative(self):
        test_dict = {(-1, -2): 'a', (0, 0): 'b', (1, 1): 'c'}
        expected_result = {(-1, -2): 'a', (0, 0): 'b', (1, 1): 'c'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_one(self):
        test_dict = {(1, 0): 'a', (2, 0): 'b', (3, 0): 'c'}
        expected_result = {(1, 0): 'a', (2, 0): 'b', (3, 0): 'c'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_corner_case_empty(self):
        test_dict = {}
        expected_result = {}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_corner_case_single_item(self):
        test_dict = {(1, 2): 'a'}
        expected_result = {(1, 2): 'a'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_invalid_input_not_mapping(self):
        with self.assertRaises(TypeError):
            sort_dict_item(123)
