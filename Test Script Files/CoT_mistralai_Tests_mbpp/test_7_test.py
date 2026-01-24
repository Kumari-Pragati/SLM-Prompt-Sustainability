import unittest
from mbpp_7_code import find_char_long

class TestFindCharLong(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(find_char_long(""), [])

    def test_single_word(self):
        self.assertListEqual(find_char_long("word"), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(find_char_long("This is a test"), ["This", "is", "a", "test"])

    def test_long_words(self):
        self.assertListEqual(find_char_long("LongWordsAreFun"), ["Long", "Words", "Are", "Fun"])

    def test_mixed_case(self):
        self.assertListEqual(find_char_long("MixedCaseIsAlsoFun"), ["Mixed", "Case", "Is", "Also", "Fun"])

    def test_punctuation(self):
        self.assertListEqual(find_char_long("This,is!a?test."), ["This", "is", "a", "test"])

    def test_multiple_spaces(self):
        self.assertListEqual(find_char_long(" This   is   a   test   "), ["This", "is", "a", "test"])

    def test_short_words(self):
        self.assertListEqual(find_char_long("one two three"), ["one", "two", "three"])

    def test_single_letter(self):
        self.assertListEqual(find_char_long("a"), ["a"])

    def test_empty_word(self):
        self.assertListEqual(find_char_long("   "), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, find_char_long, 123)
