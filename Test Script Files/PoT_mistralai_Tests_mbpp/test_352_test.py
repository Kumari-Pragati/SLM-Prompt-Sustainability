import unittest
from mbpp_352_code import unique_Characters

class TestUniqueCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(unique_Characters(''))

    def test_single_character(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertTrue(unique_Characters(char))

    def test_multiple_unique_characters(self):
        for sequence in ['abc', '123', '!@#', 'ABC', '789', 'XYZ']:
            self.assertTrue(unique_Characters(sequence))

    def test_duplicate_characters(self):
        for sequence in ['aa', '11', '!@!', 'AA', '77', 'XX']:
            self.assertFalse(unique_Characters(sequence))

    def test_long_sequence(self):
        sequence = 'a' * 100
        self.assertTrue(unique_Characters(sequence))

    def test_short_sequence(self):
        sequence = 'a'
        self.assertTrue(unique_Characters(sequence))
