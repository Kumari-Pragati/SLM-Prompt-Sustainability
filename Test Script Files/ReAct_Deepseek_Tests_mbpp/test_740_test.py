import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 'a', 2, 'b', 3, 'c')
        expected_dict = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(tuple_to_dict(test_tup), expected_dict)

    def test_empty_tuple(self):
        test_tup = ()
        expected_dict = {}
        self.assertEqual(tuple_to_dict(test_tup), expected_dict)

    def test_single_element_tuple(self):
        test_tup = (1,)
        with self.assertRaises(ValueError):
            tuple_to_dict(test_tup)

    def test_odd_length_tuple(self):
        test_tup = (1, 'a', 2)
        with self.assertRaises(ValueError):
            tuple_to_dict(test_tup)
