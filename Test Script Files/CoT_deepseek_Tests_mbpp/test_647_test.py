import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_upperstring('HelloWorldThisIsATest'), ['Hello', 'World', 'This', 'Is', 'A', 'Test'])

    def test_single_uppercase_letter(self):
        self.assertEqual(split_upperstring('A'), ['A'])

    def test_no_uppercase_letters(self):
        self.assertEqual(split_upperstring('hello world'), [])

    def test_empty_string(self):
        self.assertEqual(split_upperstring(''), [])

    def test_string_with_multiple_uppercase_letters(self):
        self.assertEqual(split_upperstring('HelloWORLDThisISATest'), ['Hello', 'WORLD', 'This', 'IS', 'A', 'Test'])

    def test_string_with_numbers(self):
        self.assertEqual(split_upperstring('HelloWorld123ThisIs456ATest'), ['Hello', 'World', 'This', 'Is', 'A', 'Test'])

    def test_string_with_special_characters(self):
        self.assertEqual(split_upperstring('Hello@World#This$Is%A&Test*'), ['Hello', 'World', 'This', 'Is', 'A', 'Test'])
