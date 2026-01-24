import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(tuple_to_dict(('a', 'b')), {'a': 'b'})
        self.assertDictEqual(tuple_to_dict(('c', 'd', 'e', 'f')), {'c': 'd', 'e': 'f'})

    def test_edge_cases(self):
        self.assertDictEqual(tuple_to_dict(('a',)), {'a': None})
        self.assertDictEqual(tuple_to_dict(('a', 'b', 'c')), {'a': 'b'})
        self.assertDictEqual(tuple_to_dict(('a', 'b', 'c', 'd', 'e')), {'a': 'b', 'c': 'd'})

    def test_complex(self):
        self.assertDictEqual(tuple_to_dict(('a', 1, 'b', 2, 'c', 3)), {'a': 1, 'b': 2, 'c': 3})
        self.assertDictEqual(tuple_to_dict(('a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5)), {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
