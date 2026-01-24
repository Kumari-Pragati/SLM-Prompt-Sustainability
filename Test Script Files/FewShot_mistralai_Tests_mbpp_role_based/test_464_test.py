import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_all_values_equal(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_some_values_not_equal(self):
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 1}, 1))

    def test_empty_dictionary(self):
        self.assertFalse(check_value({}, 1))

    def test_none_value(self):
        self.assertRaises(TypeError, check_value, {'a': None, 'b': None}, None)

    def test_non_iterable_value(self):
        self.assertRaises(TypeError, check_value, {'a': 'string', 'b': 'string'}, 'string')
