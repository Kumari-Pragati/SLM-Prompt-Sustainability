import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(is_upper(''), True)

    def test_lowercase_string(self):
        self.assertEqual(is_upper('hello'), False)

    def test_mixed_case_string(self):
        self.assertEqual(is_upper('HeLlo WoRlD'), True)

    def test_all_uppercase_string(self):
        self.assertEqual(is_upper('HELLO WORLD'), True)

    def test_none_type(self):
        self.assertRaises(TypeError, is_upper, None)

    def test_integer_type(self):
        self.assertRaises(TypeError, is_upper, 123)
