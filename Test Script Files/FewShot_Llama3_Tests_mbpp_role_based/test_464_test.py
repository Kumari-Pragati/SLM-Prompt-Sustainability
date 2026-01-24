import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):
    def test_all_values_match(self):
        dict = {'a': 1, 'b': 1, 'c': 1}
        self.assertTrue(check_value(dict, 1))

    def test_no_values_match(self):
        dict = {'a': 1, 'b': 2, 'c': 3}
        self.assertFalse(check_value(dict, 1))

    def test_all_values_match_with_empty_dict(self):
        dict = {}
        self.assertTrue(check_value(dict, None))

    def test_dict_with_non_integer_values(self):
        dict = {'a': '1', 'b': '2', 'c': '3'}
        self.assertFalse(check_value(dict, 1))

    def test_dict_with_non_dict_input(self):
        with self.assertRaises(TypeError):
            check_value(123, 1)
