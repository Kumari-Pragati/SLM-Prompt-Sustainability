import unittest
from mbpp_698_code import sort_dict_item

class TestSortDictItem(unittest.TestCase):

    def test_typical_case(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(sort_dict_item(test_dict), {'a': 1, 'b': 2, 'c': 3})

    def test_edge_case(self):
        test_dict = {'a': 1, 'b': 2}
        self.assertEqual(sort_dict_item(test_dict), {'a': 1, 'b': 2})

    def test_edge_case2(self):
        test_dict = {'a': 3, 'b': 2, 'c': 1}
        self.assertEqual(sort_dict_item(test_dict), {'c': 1, 'b': 2, 'a': 3})

    def test_edge_case3(self):
        test_dict = {}
        self.assertEqual(sort_dict_item({}), {})

    def test_edge_case4(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        self.assertEqual(sort_dict_item(test_dict), {'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1})

    def test_edge_case5(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
        self.assertEqual(sort_dict_item(test_dict), {'f': 6, 'e': 5, 'd': 4, 'c': 3, 'b': 2, 'a': 1})
