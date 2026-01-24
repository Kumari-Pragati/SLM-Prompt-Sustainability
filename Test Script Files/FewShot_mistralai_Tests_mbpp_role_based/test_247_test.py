import unittest
from mbpp_247_code import lps

class TestLPS(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lps(''), 0)

    def test_single_character_string(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(lps(char), 1)

    def test_palindrome(self):
        self.assertEqual(lps('level'), 5)
        self.assertEqual(lps('madam'), 4)

    def test_longer_palindrome(self):
        self.assertEqual(lps('racecar'), 6)
        self.assertEqual(lps('radar'), 4)

    def test_non_palindrome(self):
        self.assertEqual(lps('hello'), 1)
        self.assertEqual(lps('programming'), 3)

    def test_long_string(self):
        self.assertEqual(lps('mississippi'), 7)
