import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Len_Even("This is a test string"), "is")

    def test_even_length_word(self):
        self.assertEqual(find_Max_Len_Even("EvenLengthWord"), "EvenLengthWord")

    def test_no_even_length_words(self):
        self.assertEqual(find_Max_Len_Even("NoEvenLengthWordsHere"), "-1")

    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_single_character(self):
        self.assertEqual(find_Max_Len_Even("a"), "-1")

    def test_multiple_even_length_words(self):
        self.assertEqual(find_Max_Len_Even("This is a test string with multiple even length words"), "is")

    def test_spaces_between_words(self):
        self.assertEqual(find_Max_Len_Even("This is a test string with spaces between words"), "is")

    def test_special_characters(self):
        self.assertEqual(find_Max_Len_Even("This!@#$%^&*()is a test string with special characters"), "is")
