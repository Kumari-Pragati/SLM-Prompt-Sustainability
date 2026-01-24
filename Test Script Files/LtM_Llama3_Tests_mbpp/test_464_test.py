import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_simple_valid_input(self):
        dict = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(dict, 1))

    def test_empty_dict(self):
        dict = {}
        self.assertFalse(check_value(dict, 1))

    def test_dict_with_non_integer_values(self):
        dict = {'a': 'a', 'b': 'b', 'c': 1}
        self.assertFalse(check_value(dict, 1))

    def test_dict_with_non_integer_keys(self):
        dict = {'a': 1, 'b': 1, 'c': 'c'}
        self.assertFalse(check_value(dict, 1))

    def test_dict_with_mixed_types(self):
        dict = {'a': 1, 'b': 'b', 'c': 2}
        self.assertFalse(check_value(dict, 1))

    def test_dict_with_all_non_integer_values(self):
        dict = {'a': 'a', 'b': 'b', 'c': 'c'}
        self.assertFalse(check_value(dict, 1))

    def test_dict_with_all_integer_values(self):
        dict = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(dict, 1))
