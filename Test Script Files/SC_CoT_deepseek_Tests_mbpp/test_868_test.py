import unittest

from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(length_Of_Last_Word("Hello World"), 5)

    def test_edge_case_single_word(self):
        self.assertEqual(length_Of_Last_Word("Python"), 6)

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(length_Of_Last_Word("   Hello   World   "), 5)

    def test_edge_case_no_spaces(self):
        self.assertEqual(length_Of_Last_Word("NoSpaces"), 9)

    def test_edge_case_empty_string(self):
        self.assertEqual(length_Of_Last_Word(""), 0)

    def test_edge_case_all_spaces(self):
        self.assertEqual(length_Of_Last_Word("   "), 0)

    def test_corner_case_leading_trailing_spaces(self):
        self.assertEqual(length_Of_Last_Word("   Hello World   "), 5)

    def test_corner_case_single_character_spaces(self):
        self.assertEqual(length_Of_Last_Word("H e l l o   W o r l d"), 5)

    def test_corner_case_mixed_case(self):
        self.assertEqual(length_Of_Last_Word("hEllO WoRlD"), 5)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            length_Of_Last_Word(None)
