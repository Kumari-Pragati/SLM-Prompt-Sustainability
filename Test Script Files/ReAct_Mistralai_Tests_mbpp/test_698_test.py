import unittest
from mbpp_698_code import range
from 698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_sort_dict_item_positive(self):
        test_dict = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}
        expected_result = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c'}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_item_empty(self):
        test_dict = {}
        expected_result = {}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_item_single_item(self):
        test_dict = {(1, 2): 'a'}
        expected_result = {(1, 2): 'a'}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_item_negative(self):
        test_dict = {(0, 0): 'a', (0, -1): 'b', (-1, 0): 'c'}
        expected_result = {(-1, 0): 'c', (0, -1): 'b', (0, 0): 'a'}
        self.assertEqual(sort_dict_item(test_dict), expected_result)

    def test_sort_dict_item_key_error(self):
        test_dict = {(1, 2): 'a', (3, 4): 'b', (5, 6): 'c', (7, 0): 'd'}
        with self.assertRaises(TypeError):
            sort_dict_item(test_dict)

    def test_sort_dict_item_value_error(self):
        test_dict = {(1, 2): 1, (3, 4): 2, (5, 6): 3}
        with self.assertRaises(TypeError):
            sort_dict_item(test_dict)
