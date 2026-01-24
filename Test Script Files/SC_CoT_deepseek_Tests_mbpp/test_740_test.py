import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 'a', 2, 'b', 3, 'c')
        expected_output = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(tuple_to_dict(test_tup), expected_output)

    def test_odd_length_tuple(self):
        test_tup = (1, 'a', 2, 'b', 3, 'c', 4)
        expected_output = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(tuple_to_dict(test_tup), expected_output)

    def test_empty_tuple(self):
        test_tup = ()
        expected_output = {}
        self.assertEqual(tuple_to_dict(test_tup), expected_output)

    def test_single_element_tuple(self):
        test_tup = (1,)
        expected_output = {}
        self.assertEqual(tuple_to_dict(test_tup), expected_output)

    def test_invalid_input(self):
        test_tup = (1, 2, 3)
        with self.assertRaises(TypeError):
            tuple_to_dict(test_tup)
