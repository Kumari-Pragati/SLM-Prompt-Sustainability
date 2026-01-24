import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(find_char(""), [])

    def test_single_word(self):
        self.assertListEqual(find_char("word"), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(find_char("This is a test"), ["This", "is", "a", "test"])

    def test_long_word(self):
        self.assertListEqual(find_char("Thisisatestwithalongword"), ["Thisisatest", "with", "alongword"])

    def test_punctuation(self):
        self.assertListEqual(find_char("This, is a test."), ["This", "is", "a", "test"])

    def test_numbers(self):
        self.assertListEqual(find_char("This123isatest"), ["This", "is", "test"])

    def test_mixed_case(self):
        self.assertListEqual(find_char("THiS iS a TeSt"), ["THiS", "iS", "a", "TeSt"])
