import unittest
from mbpp_557_code import toggle_string

class TestToggleString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(toggle_string('Hello World'), 'hELLO wORLD')

    def test_empty_string(self):
        self.assertEqual(toggle_string(''), '')

    def test_string_with_numbers(self):
        self.assertEqual(toggle_string('123456'), '123456')

    def test_string_with_special_characters(self):
        self.assertEqual(toggle_string('!@#$%^&*()'), '!@#$%^&*()')

    def test_string_with_mixed_case(self):
        self.assertEqual(toggle_string('HeLLo WoRLd'), 'hEllO wOrLd')
