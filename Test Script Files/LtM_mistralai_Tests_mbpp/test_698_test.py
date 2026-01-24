import unittest
from mbpp_698_code import tuple
from six.moves.range import range

from698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_simple_case(self):
        test_dict = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}
        expected_result = {('21', '1'): 'a', ('43', '3'): 'b', ('65', '5'): 'c'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_zero(self):
        test_dict = {(0, 1): 'a', (3, 4): 'b', (5, 6): 'c'}
        expected_result = {('10', '0'): 'a', ('43', '3'): 'b', ('65', '5'): 'c'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_edge_case_negative(self):
        test_dict = {(-1, 2): 'a', (3, -4): 'b', (5, 6): 'c'}
        expected_result = {('-21', '-1'): 'a', ('-43', '3'): 'b', ('65', '5'): 'c'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_empty_dict(self):
        test_dict = {}
        expected_result = {}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_single_item_dict(self):
        test_dict = {(1, 2): 'a'}
        expected_result = {('21', '1'): 'a'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)

    def test_complex_case(self):
        test_dict = {(1, 2): 'a', (1, 3): 'b', (1, 4): 'c', (2, 1): 'd', (2, 2): 'e'}
        expected_result = {('12', '1'): 'a', ('13', '1'): 'b', ('14', '1'): 'c', ('21', '2'): 'd', ('22', '2'): 'e'}
        self.assertDictEqual(sort_dict_item(test_dict), expected_result)
