import unittest
from mbpp_740_code import tuple_to_dict

class TestTupleToDict(unittest.TestCase):

    def test_typical_input(self):
        test_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.assertEqual(tuple_to_dict(test_tup), {1: 2, 3: 4, 5: 6, 7: 8, 9: 10})

    def test_edge_case_single_element(self):
        test_tup = (1,)
        self.assertEqual(tuple_to_dict(test_tup), {1: 1})

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        self.assertEqual(tuple_to_dict(test_tup), {})

    def test_edge_case_single_element_with_value(self):
        test_tup = (1, 1)
        self.assertEqual(tuple_to_dict(test_tup), {1: 1})

    def test_edge_case_single_element_with_value_with_non_integer(self):
        test_tup = ('a', 'a')
        self.assertEqual(tuple_to_dict(test_tup), {'a': 'a'})

    def test_invalid_input_non_tuple(self):
        test_tup = 'not a tuple'
        with self.assertRaises(TypeError):
            tuple_to_dict(test_tup)

    def test_invalid_input_non_iterable(self):
        test_tup = 123
        with self.assertRaises(TypeError):
            tuple_to_dict(test_tup)
