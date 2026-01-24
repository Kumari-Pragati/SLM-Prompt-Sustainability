import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):
    def test_even_length_tuple(self):
        self.assertEqual(tuple_to_dict(('a', 'b')), {'a': 'b'})
        self.assertEqual(tuple_to_dict(('x', 'y', 'z')), {'x': 'y'})

    def test_odd_length_tuple(self):
        self.assertRaises(ValueError, tuple_to_dict, ('a', 'b', 'c'))

    def test_empty_tuple(self):
        self.assertRaises(ValueError, tuple_to_dict, ())

    def test_single_element_tuple(self):
        self.assertRaises(ValueError, tuple_to_dict, ('a',))
