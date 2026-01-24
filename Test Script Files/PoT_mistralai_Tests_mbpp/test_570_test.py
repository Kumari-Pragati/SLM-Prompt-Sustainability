import unittest
from mbpp_570_code import remove_words

class TestRemoveWords(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_words(["hello world", "apple banana", "cat dog"], ["o", "a"]), ["hello", "cat"])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_words([], ["o", "a"]), [])

    def test_edge_case_empty_charlist(self):
        self.assertEqual(remove_words(["hello", "apple", "cat"], []), ["hello", "apple", "cat"])

    def test_edge_case_single_word(self):
        self.assertEqual(remove_words(["hello"], ["o"]), [""])

    def test_edge_case_single_char_in_word(self):
        self.assertEqual(remove_words(["hello", "apple"], ["l"]), ["", "pple"])

    def test_corner_case_multiple_chars_in_word(self):
        self.assertEqual(remove_words(["hello", "apple"], ["ll", "pp"]), ["", "app"])
