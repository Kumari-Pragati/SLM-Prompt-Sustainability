import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_all_values_equal(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_all_values_not_equal(self):
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 3}, 1))

    def test_empty_dict(self):
        self.assertTrue(check_value({}, 0))

    def test_dict_with_single_value(self):
        self.assertTrue(check_value({'a': 1}, 1))

    def test_dict_with_multiple_values(self):
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 3}, 4))

    def test_dict_with_non_integer_values(self):
        self.assertFalse(check_value({'a': 'a', 'b': 'b', 'c': 'c'}, 1))

    def test_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            check_value(123, 1)
