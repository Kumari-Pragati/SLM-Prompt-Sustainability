import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, {'a': 'b', 'c': 'd'}))

    def test_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ({'a': 'b', 'c': 'd'},))

    def test_non_empty_tuple(self):
        test_tup = (1, 2, 3, 4)
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (1, 2, 3, 4, {'a': 'b', 'c': 'd'}))

    def test_non_dict_input(self):
        test_tup = (1, 2, 3)
        test_str = 'hello'
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_str)
