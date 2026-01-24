import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ((1, 2, 3), {'a': 1, 'b': 2}))

    def test_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, (test_dict,))

    def test_single_element_tuple(self):
        test_tup = (1,)
        test_dict = {'a': 1, 'b': 2}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertEqual(result, ((1,), {'a': 1, 'b': 2}))

    def test_none_input(self):
        with self.assertRaises(TypeError):
            add_dict_to_tuple(None, {'a': 1, 'b': 2})

    def test_dict_input(self):
        with self.assertRaises(TypeError):
            add_dict_to_tuple((1, 2, 3), None)
