import unittest
from mbpp_740_code import Tuple

from 740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertIsNone(tuple_to_dict(()))

    def test_single_element_tuple(self):
        self.assertIsNone(tuple_to_dict((1,)))

    def test_odd_length_tuple(self):
        self.assertRaises(ValueError, tuple_to_dict, (1, 2, 3))

    def test_even_length_tuple(self):
        self.assertEqual(tuple_to_dict((1, 'a')), {'1': 'a'})
        self.assertEqual(tuple_to_dict((1, 2, 'a', 3)), {'1': 2, '3': 'a'})
        self.assertEqual(tuple_to_dict((1, 2, 'a', 3, 4)), {'1': 2, '3': 'a'})
