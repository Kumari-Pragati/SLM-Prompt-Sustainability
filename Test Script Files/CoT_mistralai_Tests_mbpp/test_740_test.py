import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertIsNone(tuple_to_dict(()))

    def test_single_element_tuple(self):
        self.assertIsNone(tuple_to_dict((1,)))

    def test_odd_length_tuple(self):
        self.assertIsNone(tuple_to_dict((1, 2, 3)))

    def test_even_length_tuple(self):
        self.assertIsInstance(tuple_to_dict((1, 'a')), dict)
        self.assertEqual(tuple_to_dict((1, 'a')), {'1': 'a'})

    def test_mixed_types_tuple(self):
        self.assertIsInstance(tuple_to_dict((1, 'a', 2.0)), dict)
        self.assertEqual(tuple_to_dict((1, 'a', 2.0)), {'1': 'a', 2.0: None})

    def test_negative_index_tuple(self):
        self.assertIsNone(tuple_to_dict((1, 2, 3, 4, 5), -1))

    def test_out_of_range_index_tuple(self):
        self.assertIsNone(tuple_to_dict((1, 2, 3, 4, 5), 6))
