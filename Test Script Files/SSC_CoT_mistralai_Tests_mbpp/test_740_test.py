import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_normal_input(self):
        self.assertDictEqual(tuple_to_dict(('a', 'b', 'c', 'd')), {'a': 'b'})
        self.assertDictEqual(tuple_to_dict(('x', 1, 'y', 2)), {'x': 1, 'y': 2})

    def test_edge_and_boundary_conditions(self):
        self.assertDictEqual(tuple_to_dict(()), {})
        self.assertDictEqual(tuple_to_dict(('a',)), {'a': None})
        self.assertDictEqual(tuple_to_dict(('a', 'b', 'c')), {'a': 'b'})
        self.assertDictEqual(tuple_to_dict(('a', 'b', 'c', 'd', 'e')), {'a': 'b', 'c': 'd'})

    def test_special_cases(self):
        self.assertDictEqual(tuple_to_dict(('a', None, 'b')), {'a': None, 'b': None})
        self.assertDictEqual(tuple_to_dict(('a', 'b', None)), {'a': 'b'})
        self.assertDictEqual(tuple_to_dict(('', 'b')), {'': 'b'})
