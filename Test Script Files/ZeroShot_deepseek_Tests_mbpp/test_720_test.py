import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_add_dict_to_tuple(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 4, 'b': 5}
        expected_output = (1, 2, 3, {'a': 4, 'b': 5})
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)

    def test_add_dict_to_tuple_empty_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {}
        expected_output = (1, 2, 3, {})
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)

    def test_add_dict_to_tuple_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 4, 'b': 5}
        expected_output = ({'a': 4, 'b': 5},)
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)
