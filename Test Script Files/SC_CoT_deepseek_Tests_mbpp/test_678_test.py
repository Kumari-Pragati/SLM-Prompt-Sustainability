import unittest
from mbpp_678_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_spaces('hello world'), 'helloworld')

    def test_empty_string(self):
        self.assertEqual(remove_spaces(''), '')

    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces('helloworld'), 'helloworld')

    def test_string_with_multiple_spaces(self):
        self.assertEqual(remove_spaces('hello   world'), 'helloworld')

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces('   hello world   '), 'helloworld')

    def test_special_characters(self):
        self.assertEqual(remove_spaces('hello@world'), 'helloworld')

    def test_numbers_in_string(self):
        self.assertEqual(remove_spaces('hello123world456'), 'helloworld')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_spaces(12345)
