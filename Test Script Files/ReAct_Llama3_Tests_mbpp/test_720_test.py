import unittest
from mbpp_720_code import add_dict_to_tuple

class TestAddDictToTuple(unittest.TestCase):
    def test_typical_case(self):
        test_tup = (1, 2, 3)
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), len(test_tup) + 1)
        self.assertEqual(result[-1], test_dict)

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        test_dict = {'a': 'b', 'c': 'd'}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], test_dict)

    def test_edge_case_empty_dict(self):
        test_tup = (1, 2, 3)
        test_dict = {}
        result = add_dict_to_tuple(test_tup, test_dict)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), len(test_tup))
        self.assertEqual(result, test_tup)

    def test_error_case_non_tuple_input(self):
        test_tup = 'not a tuple'
        test_dict = {'a': 'b', 'c': 'd'}
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_dict)

    def test_error_case_non_dict_input(self):
        test_tup = (1, 2, 3)
        test_dict = 'not a dict'
        with self.assertRaises(TypeError):
            add_dict_to_tuple(test_tup, test_dict)
