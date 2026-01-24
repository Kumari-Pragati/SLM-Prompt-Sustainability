import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):

    def test_toggle_string_lowercase(self):
        self.assertEqual(toggle_string('hello'), 'HELLO')

    def test_toggle_string_uppercase(self):
        self.assertEqual(toggle_string('HELLO'), 'hello')

    def test_toggle_string_mixedcase(self):
        self.assertEqual(toggle_string('HeLlO'), 'hElLo')

    def test_toggle_string_empty(self):
        self.assertEqual(toggle_string(''), '')

    def test_toggle_string_special_characters(self):
        self.assertEqual(toggle_string('h@ll0'), 'H@LL0')

    def test_toggle_string_numbers(self):
        self.assertEqual(toggle_string('12345'), '12345')

    def test_toggle_string_whitespace(self):
        self.assertEqual(toggle_string('hello world'), 'HELLO WORLD')
