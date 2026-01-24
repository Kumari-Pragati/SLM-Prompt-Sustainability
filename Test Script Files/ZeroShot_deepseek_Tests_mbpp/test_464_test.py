import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_all_values_are_same(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_not_all_values_are_same(self):
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 1}, 1))

    def test_empty_dict(self):
        self.assertTrue(check_value({}, 0))

    def test_all_values_are_same_with_zero(self):
        self.assertTrue(check_value({'a': 0, 'b': 0, 'c': 0}, 0))

    def test_negative_values(self):
        self.assertTrue(check_value({'a': -1, 'b': -1, 'c': -1}, -1))

    def test_mixed_positive_and_negative_values(self):
        self.assertFalse(check_value({'a': 1, 'b': -1, 'c': 1}, 1))
