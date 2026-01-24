import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_length("word word word", 3), "word word")
        self.assertEqual(remove_length("word word word word", 3), "word word")
        self.assertEqual(remove_length("word word word word word", 3), "word word word")

    def test_edge_case_short_string(self):
        self.assertEqual(remove_length("a", 3), "")
        self.assertEqual(remove_length("a b", 3), "b")
        self.assertEqual(remove_length("a b c", 3), "a b c")

    def test_edge_case_long_string(self):
        self.assertEqual(remove_length("word word word word word word word word", 3), "word word word word word word")
        self.assertEqual(remove_length("word word word word word word word word word", 4), "word word word word word word word")
        self.assertEqual(remove_length("word word word word word word word word word word", 4), "word word word word word word word word")

    def test_corner_case_empty_list(self):
        self.assertEqual(remove_length("", 3), "")
        self.assertEqual(remove_length(" ", 3), "")

    def test_corner_case_single_word(self):
        self.assertEqual(remove_length("word", 3), "")
        self.assertEqual(remove_length("Word", 3), "")
