import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_simple(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 1, 'b': 2}))

    def test_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ({'a': 1, 'b': 2},))

    def test_empty_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {}))

    def test_dict_with_tuple(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': (4, 5, 6)}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': (4, 5, 6)}))

    def test_dict_with_list(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': [4, 5, 6]}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': [4, 5, 6]}))
