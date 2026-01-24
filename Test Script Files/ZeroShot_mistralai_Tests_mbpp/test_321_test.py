import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(find_demlo(char), str(1))

    def test_multiple_characters_string(self):
        test_strings = [
            "ab", "abc", "xyz", "123", "abc123", "123abc", "0123456789",
            "01234567890", "a1b2c3", "z9y8x7", "12345678901234567890"
        ]
        for test_string in test_strings:
            self.assertEqual(find_demlo(test_string), "".join(str(i) for i in range(len(test_string) * 2)))
