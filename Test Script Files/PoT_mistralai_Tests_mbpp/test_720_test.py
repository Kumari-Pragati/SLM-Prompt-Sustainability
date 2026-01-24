import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_dict_to_tuple((1, 2, 3), {'a': 4}), (1, 2, 3, {'a': 4}))

    def test_empty_tuple(self):
        self.assertEqual(add_dict_toTuple((), {'a': 4}), ('a': 4))

    def test_single_element_tuple(self):
        self.assertEqual(add_dict_toTuple((1,), {'a': 4}), (1, {'a': 4}))

    def test_negative_integer_dict_key(self):
        self.assertEqual(add_dict_toTuple((1, 2, 3), {'-1': 4}), (1, 2, 3, {'-1': 4}))

    def test_empty_dict(self):
        self.assertEqual(add_dict_toTuple((1, 2, 3), {}), (1, 2, 3))

    def test_key_not_in_dict(self):
        self.assertEqual(add_dict_toTuple((1, 2, 3), {'a': 4, 'b': 5}), (1, 2, 3, {'a': 4, 'b': 5}))
