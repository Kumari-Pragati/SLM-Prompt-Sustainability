import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertEqual(tuple_to_dict(('a', 1, 'b', 2)), {'a': 1, 'b': 2})

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_dict(()), {})

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_dict(('a',)), {})

    def test_odd_length_tuple(self):
        self.assertEqual(tuple_to_dict(('a', 1, 'b')), {'a': 1})

    def test_duplicate_keys(self):
        self.assertEqual(tuple_to_dict(('a', 1, 'a', 2)), {'a': 2})

    def test_large_tuple(self):
        large_tuple = tuple(range(1000))
        self.assertEqual(tuple_to_dict(large_tuple), {})
