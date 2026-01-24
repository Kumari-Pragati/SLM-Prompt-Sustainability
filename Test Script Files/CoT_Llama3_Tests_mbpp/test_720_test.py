import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_typical_input(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 1, 'b': 2}))

    def test_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ({'a': 1, 'b': 2},))

    def test_non_empty_tuple(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 1, 'b': 2}))

    def test_non_dict_input(self):
        test_tup = (1, 2, 3)
        test_dict = 'not a dict'
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_dict)

    def test_non_tuple_input(self):
        test_tup = 'not a tuple'
        test_dict = {'a': 1, 'b': 2}
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_dict)
