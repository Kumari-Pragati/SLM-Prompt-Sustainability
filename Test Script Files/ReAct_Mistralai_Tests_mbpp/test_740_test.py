import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertDictEqual(tuple_to_dict(()), {})

    def test_single_element_tuple(self):
        self.assertDictEqual(tuple_to_dict((1,)), {'1': None})

    def test_single_key_single_value_tuple(self):
        self.assertDictEqual(tuple_to_dict((1, 'a')), {'1': 'a'})

    def test_even_length_tuple(self):
        self.assertDictEqual(tuple_to_dict((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')), {'1': 'a', '2': 'b', '3': 'c', '4': 'd'})

    def test_odd_length_tuple(self):
        self.assertDictEqual(tuple_to_dict((1, 'a'), (2, 'b'), (3, 'c')), {'1': 'a', '2': 'b', '3': None})

    def test_zero_indexed_tuple(self):
        self.assertDictEqual(tuple_to_dict((0, 'z')), {'0': 'z'})

    def test_negative_indexed_tuple(self):
        self.assertDictEqual(tuple_to_dict((-1, 'x')), {'0': 'x'})

    def test_empty_key_tuple(self):
        self.assertRaises(KeyError, tuple_to_dict, ((None, 'a'), (2, 'b')))

    def test_empty_value_tuple(self):
        self.assertRaises(TypeError, tuple_to_dict, ((1, None), (2, 'b')))
