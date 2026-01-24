import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_demlo(""), "")

    def test_single_character_string(self):
        self.assertEqual(find_demlo("a"), "1")

    def test_positive_numbers_string(self):
        self.assertEqual(find_demlo("12345"), "123542")

    def test_negative_numbers_string(self):
        self.assertEqual(find_demlo("abc-123"), "123abc")

    def test_mixed_characters_and_numbers_string(self):
        self.assertEqual(find_demlo("a1b2c3"), "123c3b2a")

    def test_long_string(self):
        self.assertEqual(find_demlo("012345678901234567890"), "012345678901234567890")
