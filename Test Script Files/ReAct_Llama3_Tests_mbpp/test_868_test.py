import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(length_Of_Last_Word("Hello World"), 5)

    def test_edge_case_empty_string(self):
        self.assertEqual(length_Of_Last_Word(""), 0)

    def test_edge_case_single_word(self):
        self.assertEqual(length_Of_Last_Word("Hello"), 5)

    def test_edge_case_single_space(self):
        self.assertEqual(length_Of_Last_Word("   "), 0)

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World   "), 5)

    def test_edge_case_no_spaces(self):
        self.assertEqual(length_Of_Last_Word("HelloWorld"), 10)

    def test_edge_case_multiple_words(self):
        self.assertEqual(length_Of_Last_Word("Hello World is fun"), 7)

    def test_edge_case_multiple_spaces_between_words(self):
        self.assertEqual(length_Of_Last_Word("Hello   World   is   fun"), 7)

    def test_edge_case_multiple_spaces_at_end(self):
        self.assertEqual(length_Of_Last_Word("Hello   World   is   fun   "), 7)

    def test_edge_case_multiple_spaces_at_start(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World   is   fun   "), 7)

    def test_edge_case_multiple_spaces_at_start_and_end(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World   is   fun   "), 7)

    def test_edge_case_multiple_spaces_between_words_and_at_end(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World   is   fun   "), 7)

    def test_edge_case_multiple_spaces_between_words_and_at_start(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World   is   fun   "), 7)

    def test_edge_case_multiple_spaces_between_words_and_at_start_and_end(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World   is   fun   "), 7)
