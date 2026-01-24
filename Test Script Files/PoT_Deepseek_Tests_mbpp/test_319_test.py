import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_long_word("Hello world"), ['Hello'])

    def test_edge_case_single_word(self):
        self.assertEqual(find_long_word("Python"), ['Python'])

    def test_boundary_case_five_letter_word(self):
        self.assertEqual(find_long_word("Programming"), ['Programming'])

    def test_edge_case_no_words(self):
        self.assertEqual(find_long_word(""), [])

    def test_corner_case_multiple_five_letter_words(self):
        self.assertEqual(find_long_word("Hello there programming"), ['Hello', 'there', 'program'])

    def test_corner_case_mixed_case(self):
        self.assertEqual(find_long_word("Hello There Programming"), ['Hello', 'There', 'Programmin'])

    def test_corner_case_special_characters(self):
        self.assertEqual(find_long_word("Hello@there!programming"), ['Hello', 'there'])
