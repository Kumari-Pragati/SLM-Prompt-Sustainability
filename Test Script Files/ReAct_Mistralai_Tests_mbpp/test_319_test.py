import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(find_long_word(""), [])

    def test_single_word(self):
        self.assertListEqual(find_long_word("short"), ["short"])
        self.assertListEqual(find_long_word("long"), ["long"])

    def test_multiple_words(self):
        self.assertListEqual(find_long_word("shortlongshort"), ["long"])
        self.assertListEqual(find_long_word("longshortlong"), ["long", "short"])

    def test_long_word_at_beginning(self):
        self.assertListEqual(find_long_word("longwordshort"), ["longword"])

    def test_long_word_at_end(self):
        self.assertListEqual(find_long_word("shortwordlong"), ["longword"])

    def test_long_word_in_middle(self):
        self.assertListEqual(find_long_word("shortwordlongshort"), ["longword"])

    def test_word_exactly_5_characters(self):
        self.assertListEqual(find_long_word("word12345"), ["word12345"])

    def test_word_longer_than_5_characters(self):
        self.assertListEqual(find_long_word("word123456"), [])

    def test_word_shorter_than_5_characters(self):
        self.assertListEqual(find_long_word("word123"), [])

    def test_punctuation_at_beginning(self):
        self.assertListEqual(find_long_word("!longwordshort"), [])
        self.assertListEqual(find_long_word("longword?short"), ["longword"])
        self.assertListEqual(find_long_word("longword:short"), ["longword"])

    def test_punctuation_at_end(self):
        self.assertListEqual(find_long_word("longwordshort!"), ["longword"])
        self.assertListEqual(find_long_word("longwordshort?"), ["longword"])
        self.assertListEqual(find_long_word("longwordshort:"), ["longword"])

    def test_punctuation_in_middle(self):
        self.assertListEqual(find_long_word("longword,short"), ["longword"])
        self.assertListEqual(find_long_word("longword;short"), ["longword"])
        self.assertListEqual(find_long_word("longword!short"), ["longword"])
