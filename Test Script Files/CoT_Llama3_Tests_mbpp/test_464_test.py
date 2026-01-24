import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_true(self):
        self.assertTrue(check_value({'a': 1, 'b': 1, 'c': 1}, 1))

    def test_false(self):
        self.assertFalse(check_value({'a': 1, 'b': 2, 'c': 1}, 1))

    def test_empty_dict(self):
        self.assertFalse(check_value({}, 1))

    def test_dict_with_non_integer_values(self):
        with self.assertRaises(TypeError):
            check_value({'a': 1, 'b': 'b', 'c': 1}, 1)

    def test_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            check_value(123, 1)

    def test_dict_with_non_integer_key(self):
        with self.assertRaises(TypeError):
            check_value({'a': 1, 'b': 'b', 'c': 1}, 1)
