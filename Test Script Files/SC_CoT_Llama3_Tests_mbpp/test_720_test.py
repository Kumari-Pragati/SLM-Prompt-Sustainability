import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_typical_inputs(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 1, 'b': 2}))

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ({'a': 1, 'b': 2},))

    def test_edge_case_empty_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {}))

    def test_edge_case_dict_with_tuple(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': (2, 3)}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 1, 'b': (2, 3)}))

    def test_edge_case_tuple_with_dict(self):
        test_tup = (1, {'a': 1, 'b': 2}, 3)
        test_dict = {'c': 3, 'd': 4}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, {'a': 1, 'b': 2}, 3, {'c': 3, 'd': 4}))

    def test_edge_case_dict_with_list(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': [2, 3]}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 1, 'b': [2, 3]}))

    def test_edge_case_list_with_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': [2, 3]}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 1, 'b': [2, 3]}))

    def test_invalid_input_non_dict(self):
        test_tup = (1, 2, 3)
        test_dict = 'not a dict'
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_dict)

    def test_invalid_input_non_tuple(self):
        test_tup = 'not a tuple'
        test_dict = {'a': 1, 'b': 2}
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_dict)
