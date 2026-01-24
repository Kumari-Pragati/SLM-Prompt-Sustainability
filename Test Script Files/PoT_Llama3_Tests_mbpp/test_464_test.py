import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_typical_case(self):
        dict = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(dict, 1))

    def test_edge_case_all_values_match(self):
        dict = {'a': 2, 'b': 2, 'c': 2}
        self.assertTrue(check_value(dict, 2))

    def test_edge_case_no_values_match(self):
        dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertFalse(check_value(dict, 1))

    def test_edge_case_empty_dict(self):
        dict = {}
        self.assertTrue(check_value(dict, None))

    def test_edge_case_dict_with_none(self):
        dict = {'a': None, 'b': None, 'c': None}
        self.assertTrue(check_value(dict, None))

    def test_edge_case_dict_with_non_integer_values(self):
        dict = {'a': 'a', 'b': 'b', 'c': 'c'}
        with self.assertRaises(TypeError):
            check_value(dict, 1)

    def test_edge_case_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            check_value(123, 1)

    def test_edge_case_dict_with_non_integer_key(self):
        dict = {'a': 1, 'b': 2, 'c': 'd'}
        with self.assertRaises(TypeError):
            check_value(dict, 1)
