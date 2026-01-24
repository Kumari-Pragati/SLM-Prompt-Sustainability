import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(find_char_long(""), [])

    def test_single_char(self):
        self.assertListEqual(find_char_long("a"), [])
        self.assertListEqual(find_char_long("A"), [])

    def test_short_words(self):
        self.assertListEqual(find_char_long("ab"), [])
        self.assertListEqual(find_char_long("Ab"), [])
        self.assertListEqual(find_char_long("abcd"), [])
        self.assertListEqual(find_char_long("AbCd"), [])

    def test_long_words(self):
        self.assertListEqual(find_char_long("aaaaa"), ["aaaaa"])
        self.assertListEqual(find_char_long("AbCdEfGhIj"), ["AbCd", "EfGh", "Ij"])

    def test_mixed_case(self):
        self.assertListEqual(find_char_long("AbCdEfGhIjKlMnOp"), ["AbCd", "EfGh", "Ij", "Kl", "Mn", "Op"])

    def test_punctuation(self):
        self.assertListEqual(find_char_long("AbCd,EfGh!Ij$Kl%Mn&Op#"), ["AbCd", "EfGh", "Ij", "Kl", "Mn", "Op"])

    def test_multiple_matches(self):
        self.assertListEqual(find_char_long("aaaaabbbbccccc"), ["aaaaa", "bbbb", "ccccc"])
