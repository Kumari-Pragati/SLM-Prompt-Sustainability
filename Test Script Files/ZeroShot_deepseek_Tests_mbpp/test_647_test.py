import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperString(unittest.TestCase):

    def test_simple_string(self):
        self.assertEqual(split_upperstring('HelloWorld'), ['Hello', 'World'])

    def test_string_with_numbers(self):
        self.assertEqual(split_upperstring('HelloWorld123'), ['Hello', 'World123'])

    def test_string_with_special_characters(self):
        self.assertEqual(split_upperstring('Hello@World'), ['Hello', 'World'])

    def test_string_with_mixed_case(self):
        self.assertEqual(split_upperstring('HelloWORLD'), ['Hello', 'WORLD'])

    def test_empty_string(self):
        self.assertEqual(split_upperstring(''), [])
