import unittest
from mbpp_720_code import add_dict_toTuple

class TestAddDictToTuple(unittest.TestCase):

    def test_normal_input(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': 2}
        self.assertEqual(add_dict_toTuple(test_tup, test_dict), ((1, 2, 3), test_dict))

    def test_empty_input(self):
        test_tup = ()
        test_dict = {'a': 1, 'b': 2}
        self.assertEqual(add_dict_toTuple(test_tup, test_dict), (test_dict,))

    def test_single_input(self):
        test_tup = (1,)
        test_dict = {'a': 1, 'b': 2}
        self.assertEqual(add_dict_toTuple(test_tup, test_dict), (1, test_dict))

    def test_multiple_inputs(self):
        test_tup = (1, 2, 3)
        test_dict1 = {'a': 1, 'b': 2}
        test_dict2 = {'c': 3, 'd': 4}
        self.assertEqual(add_dict_toTuple((test_tup, test_dict1), test_dict2), ((1, 2, 3), {'a': 1, 'b': 2}, test_dict2))

    def test_key_error(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': 2, 'non_existent_key': 'error'}
        with self.assertRaises(KeyError):
            add_dict_toTuple(test_tup, test_dict)
