import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count('hello', 'l'), 2)

    def test_single_character(self):
        self.assertEqual(count('aaaaa', 'a'), 5)

    def test_no_occurrence(self):
        self.assertEqual(count('hello', 'z'), 0)

    def test_empty_string(self):
        self.assertEqual(count('', 'a'), 0)

    def test_case_sensitivity(self):
        self.assertEqual(count('Hello', 'h'), 0)

    def test_numeric_string(self):
        self.assertEqual(count('12345', '3'), 1)

    def test_special_characters(self):
        self.assertEqual(count('!@#$%', '%'), 1)

    def test_whitespace(self):
        self.assertEqual(count('hello world', ' '), 1)
