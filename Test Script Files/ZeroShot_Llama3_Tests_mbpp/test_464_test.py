import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_check_value_all_values_equal(self):
        dict = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(dict, 1))

    def test_check_value_not_all_values_equal(self):
        dict = {'a': 1, 'b': 2, 'c': 1}
        self.assertFalse(check_value(dict, 1))

    def test_check_value_empty_dict(self):
        dict = {}
        self.assertTrue(check_value(dict, None))

    def test_check_value_dict_with_none_value(self):
        dict = {'a': 1, 'b': None, 'c': 1}
        self.assertFalse(check_value(dict, 1))

    def test_check_value_dict_with_non_integer_value(self):
        dict = {'a': 1, 'b': 'hello', 'c': 1}
        self.assertFalse(check_value(dict, 1))
