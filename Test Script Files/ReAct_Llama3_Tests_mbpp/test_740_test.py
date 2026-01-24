import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8)
        result = tuple_to_dict(test_tup)
        self.assertEqual(result, {1: 2, 3: 4, 5: 6, 7: 8})

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        result = tuple_to_dict(test_tup)
        self.assertEqual(result, {})

    def test_edge_case_single_element_tuple(self):
        test_tup = (1,)
        result = tuple_to_dict(test_tup)
        self.assertEqual(result, {})

    def test_edge_case_two_element_tuple(self):
        test_tup = (1, 2)
        result = tuple_to_dict(test_tup)
        self.assertEqual(result, {1: 2})

    def test_edge_case_odd_length_tuple(self):
        test_tup = (1, 2, 3, 4, 5)
        result = tuple_to_dict(test_tup)
        self.assertEqual(result, {1: 2, 3: 4})

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_to_dict("not a tuple")
