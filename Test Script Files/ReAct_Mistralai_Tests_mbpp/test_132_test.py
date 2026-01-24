import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):

    def test_empty_tuple(self):
        """Test tup_string with an empty tuple"""
        self.assertEqual(tup_string(()), "")

    def test_single_element_tuple(self):
        """Test tup_string with a single element tuple"""
        self.assertEqual(tup_string(('a',)), 'a')

    def test_multiple_elements_tuple(self):
        """Test tup_string with a multiple elements tuple"""
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_mixed_types_tuple(self):
        """Test tup_string with a tuple containing mixed types"""
        self.assertEqual(tup_string(('a', 1, 3.14)), 'a13.14')

    def test_tuple_with_none(self):
        """Test tup_string with a tuple containing None"""
        self.assertEqual(tup_string(('a', None, 'b')), 'ab')

    def test_tuple_with_empty_string(self):
        """Test tup_string with a tuple containing an empty string"""
        self.assertEqual(tup_string(('', 'b', 'c')), 'bcc')

    def test_tuple_with_whitespace(self):
        """Test tup_string with a tuple containing whitespace"""
        self.assertEqual(tup_string(('a ', 'b', ' c')), 'ab c')

    def test_large_tuple(self):
        """Test tup_string with a large tuple"""
        large_tuple = tuple('a' * 1000)
        self.assertEqual(tup_string(large_tuple), large_tuple)

    def test_tuple_with_special_characters(self):
        """Test tup_string with a tuple containing special characters"""
        self.assertEqual(tup_string(('!@#$%^&*()_+-=',)), '!@#$%^&*()_+-=')
