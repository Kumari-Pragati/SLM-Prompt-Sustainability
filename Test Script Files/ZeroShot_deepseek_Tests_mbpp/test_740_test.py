import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_dict(()), {})

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_dict((1,)), {0: 1})

    def test_even_length_tuple(self):
        self.assertEqual(tuple_to_dict((1, 2, 3, 4)), {1: 2, 3: 4})

    def test_odd_length_tuple(self):
        self.assertEqual(tuple_to_dict((1, 2, 3)), {1: 2, 3: None})

    def test_duplicate_keys(self):
        self.assertEqual(tuple_to_dict((1, 2, 1, 3)), {1: 2, 1: 3})
