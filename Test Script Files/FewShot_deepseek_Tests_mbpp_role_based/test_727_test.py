import unittest
from mbpp_727_code import remove_char

class TestRemoveChar(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_char('Hello, World!'), 'HelloWorld')

    def test_edge_case(self):
        self.assertEqual(remove_char(''), '')

    def test_boundary_case(self):
        self.assertEqual(remove_char('a' * 10000), 'a' * 10000)

    def test_with_special_characters(self):
        self.assertEqual(remove_char('@#$%^&*()'), '')

    def test_with_numbers(self):
        self.assertEqual(remove_char('1234567890'), '1234567890')

    def test_with_mixed_characters(self):
        self.assertEqual(remove_char('abc123!@#'), 'abc123')

    def test_with_underscore(self):
        self.assertEqual(remove_char('Hello_World'), 'HelloWorld')
