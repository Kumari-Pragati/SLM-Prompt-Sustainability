import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count("", "a"), 0)

    def test_single_character(self):
        self.assertEqual(count("a", "a"), 1)
        self.assertEqual(count("A", "a"), 0)

    def test_multiple_characters(self):
        self.assertEqual(count("aaa", "a"), 3)
        self.assertEqual(count("AAA", "a"), 0)

    def test_mixed_case(self):
        self.assertEqual(count("Aa1Bb2Cc", "a"), 2)
        self.assertEqual(count("Aa1Bb2Cc", "A"), 1)
        self.assertEqual(count("Aa1Bb2Cc", "1"), 2)

    def test_special_characters(self):
        self.assertEqual(count("!@#$%^&*()_+-=", "$"), 3)
