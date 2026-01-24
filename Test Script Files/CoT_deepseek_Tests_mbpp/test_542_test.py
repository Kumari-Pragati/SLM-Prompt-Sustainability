import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(fill_spaces("Hello, world."), "Hello:world:")

    def test_multiple_spaces(self):
        self.assertEqual(fill_spaces("This is a test."), "This:is:a:test:")

    def test_no_spaces(self):
        self.assertEqual(fill_spaces("Nospaces"), "Nospaces")

    def test_empty_string(self):
        self.assertEqual(fill_spaces(""), "")

    def test_special_characters(self):
        self.assertEqual(fill_spaces("!@#$%^&*()"), "!@#$%^&*()")

    def test_numbers(self):
        self.assertEqual(fill_spaces("123 456 789"), "123:456:789")

    def test_leading_trailing_spaces(self):
        self.assertEqual(fill_spaces("   leading and trailing spaces   "), ":leading:and:trailing:spaces:")
