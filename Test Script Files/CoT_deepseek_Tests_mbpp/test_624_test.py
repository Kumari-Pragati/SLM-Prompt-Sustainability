import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(is_upper('hello'), 'HELLO')

    def test_empty_string(self):
        self.assertEqual(is_upper(''), '')

    def test_already_upper_case(self):
        self.assertEqual(is_upper('HELLO'), 'HELLO')

    def test_numeric_string(self):
        self.assertEqual(is_upper('12345'), '12345')

    def test_special_characters(self):
        self.assertEqual(is_upper('!@#$%'), '!@#$%')

    def test_mixed_case_string(self):
        self.assertEqual(is_upper('HeLlO'), 'HELLO')

    def test_none_input(self):
        with self.assertRaises(TypeError):
            is_upper(None)
