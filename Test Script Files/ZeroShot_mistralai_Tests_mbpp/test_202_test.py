import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_even(''), '')

    def test_single_character_string(self):
        for char in ['a', 'b', 'c']:
            self.assertEqual(remove_even(char), char)

    def test_even_length_string(self):
        for string in ['aa', 'ab', 'ba']:
            self.assertEqual(remove_even(string), '')

    def test_odd_length_string(self):
        for string in ['abc', 'acb', 'cba']:
            self.assertEqual(remove_even(string), string[1:-1])

    def test_mixed_case_string(self):
        for string in ['AbCdEf', 'AbCdEfGh', 'GhIjKl']:
            self.assertEqual(remove_even(string), string[1:-1].lower())
