import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_to_dict(('a', 1, 'b', 2)), {'a': 1, 'b': 2})

    def test_single_element(self):
        self.assertEqual(tuple_to_dict(('a',)), {'a': None})

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_dict(()), {})

    def test_odd_length_tuple(self):
        self.assertEqual(tuple_to_dict(('a', 1, 'b')), {'a': 1, 'b': None})

    def test_duplicate_keys(self):
        self.assertEqual(tuple_to_dict(('a', 1, 'a', 2)), {'a': 2})

    def test_non_string_keys(self):
        self.assertEqual(tuple_to_dict((1, 1, 2, 2)), {1: 1, 2: 2})

    def test_non_hashable_values(self):
        self.assertEqual(tuple_to_dict(('a', [1, 2], 'b', [3, 4])), {'a': [1, 2], 'b': [3, 4]})
