import unittest
from mbpp_464_code import check_value

class TestCheckValue(unittest.TestCase):

    def test_check_value_with_single_value(self):
        """Test check_value with a dictionary containing a single value."""
        dict_single = {'key1': 5}
        self.assertTrue(check_value(dict_single, 5))

    def test_check_value_with_multiple_values(self):
        """Test check_value with a dictionary containing multiple values."""
        dict_multiple = {'key1': 3, 'key2': 3, 'key3': 3}
        self.assertTrue(check_value(dict_multiple, 3))

    def test_check_value_with_no_matching_values(self):
        """Test check_value with a dictionary containing no matching values."""
        dict_no_match = {'key1': 1, 'key2': 2, 'key3': 4}
        self.assertFalse(check_value(dict_no_match, 3))

    def test_check_value_with_empty_dict(self):
        """Test check_value with an empty dictionary."""
        empty_dict = {}
        self.assertFalse(check_value(empty_dict, 5))

    def test_check_value_with_non_iterable_input(self):
        """Test check_value with non-iterable input."""
        non_dict = 'string'
        self.assertRaises(TypeError, check_value, non_dict, 5)

    def test_check_value_with_non_number_value(self):
        """Test check_value with a dictionary containing non-number values."""
        dict_non_number = {'key1': 'five', 'key2': 3, 'key3': 4}
        self.assertFalse(check_value(dict_non_number, 3))
