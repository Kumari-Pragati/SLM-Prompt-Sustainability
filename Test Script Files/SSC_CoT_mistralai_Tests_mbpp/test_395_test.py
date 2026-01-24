import unittest
from mbpp_395_code import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(first_non_repeating_character("abcdefghijklmn"), 'a')
        self.assertEqual(first_non_repeating_character("hello"), 'h')
        self.assertEqual(first_non_repeating_character(""), None)

    def test_edge_cases(self):
        self.assertEqual(first_non_repeating_character("aabbcc"), None)
        self.assertEqual(first_non_repeating_character("a"), 'a')
        self.assertEqual(first_non_repeating_character("aa"), None)
        self.assertEqual(first_non_repeating_character("abcabc"), 'c')

    def test_boundary_cases(self):
        self.assertEqual(first_non_repeating_character("A" * 1000), 'A')
        self.assertEqual(first_non_repeating_character("z" * 1000), 'z')
        self.assertEqual(first_non_repeating_character("0123456789" * 100), '0')

    def test_special_cases(self):
        self.assertEqual(first_non_repeating_character("aA1B1bB1"), '1')
        self.assertEqual(first_non_repeating_character("1234567890"), '1')
        self.assertEqual(first_non_repeating_character("!@#$%^&*()_+-=[]{};:'\",.<>?/"), '!')
