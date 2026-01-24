import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_empty_tuple_and_dict(self):
        self.assertEqual(add_dict_to_tuple((), {}), ({},))

    def test_single_element_tuple_and_dict(self):
        self.assertEqual(add_dict_toTuple((1,), {'a': 1}), (1, {'a': 1}))

    def test_multiple_elements_tuple_and_dict(self):
        self.assertEqual(add_dict_toTuple((1, 2, 3), {'a': 1, 'b': 2}), (1, 2, 3, {'a': 1, 'b': 2}))

    def test_tuple_with_dict_as_element(self):
        self.assertEqual(add_dict_toTuple(({'a': 1},), {}), ({'a': 1},))

    def test_tuple_with_multiple_dicts_as_elements(self):
        self.assertEqual(add_dict_toTuple(({'a': 1}, {'b': 2}), {}), ({'a': 1}, {'b': 2},))

    def test_none_input(self):
        self.assertRaises(TypeError, add_dict_toTuple, None, {})

    def test_string_input(self):
        self.assertRaises(TypeError, add_dict_toTuple, ('str',), {})

    def test_list_input(self):
        self.assertRaises(TypeError, add_dict_toTuple, [1, 2, 3], {})
