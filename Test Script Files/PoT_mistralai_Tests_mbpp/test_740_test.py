import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):
    def test_typical_case(self):
        self.assertDictEqual(tuple_to_dict(('a', 'b', 'c', 'd')), {'a': 'b'})
        self.assertDictEqual(tuple_to_dict(('x', 1, 'y', 2)), {'x': 1, 'y': 2})

    def test_edge_case_odd_length(self):
        self.assertDictEqual(tuple_to_dict(('a', 'b', 'c')), {'a': 'b'})

    def test_edge_case_even_length_2(self):
        self.assertDictEqual(tuple_to_dict(('a', 'b')), {'a': 'b'})

    def test_corner_case_empty_tuple(self):
        self.assertIsNone(tuple_to_dict(()))

    def test_corner_case_single_element(self):
        self.assertIsNone(tuple_to_dict(('a',)))
