import unittest
from mbpp_477_code import is_lower

class TestIsLower(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(is_lower('Hello'), 'hello')

    def test_already_lowercase(self):
        self.assertEqual(is_lower('hello'), 'hello')

    def test_empty_string(self):
        self.assertEqual(is_lower(''), '')

    def test_special_characters(self):
        self.assertEqual(is_lower('@#$%^&*()'), '@#$%^&*()')

    def test_numbers_and_symbols(self):
        self.assertEqual(is_lower('1234567890!@#$%^&*()'), '1234567890!@#$%^&*()')

    def test_mixed_case(self):
        self.assertEqual(is_lower('HeLlO'), 'hello')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_lower(12345)
