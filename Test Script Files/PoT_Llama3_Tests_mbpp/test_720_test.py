import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_typical_case(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 'b', 'c': 'd'}))

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ({'a': 'b', 'c': 'd'},))

    def test_edge_case_empty_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {}))

    def test_edge_case_dict_with_single_element_tuple(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': (4, 5, 6)}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': (4, 5, 6)}))

    def test_edge_case_tuple_with_dict(self):
        test_tup = ({'a': 'b', 'c': 'd'},)
        test_dict = {'e': 'f'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ({'a': 'b', 'c': 'd'}, {'e': 'f'}))
