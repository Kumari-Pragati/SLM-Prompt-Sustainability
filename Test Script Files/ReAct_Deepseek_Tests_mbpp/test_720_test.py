import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 4}
        expected_output = (1, 2, 3, {'a': 4})
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)

    def test_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 4}
        expected_output = ({'a': 4},)
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)

    def test_empty_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {}
        expected_output = (1, 2, 3)
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)

    def test_large_tuple(self):
        test_tup = tuple(range(1, 1001))
        test_dict = {'a': 4}
        expected_output = test_tup + (test_dict,)
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)

    def test_nested_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': {'b': 4}}
        expected_output = (1, 2, 3, {'a': {'b': 4}})
        self.assertEqual(add_dict_to_tuple(test_tup, test_dict), expected_output)
