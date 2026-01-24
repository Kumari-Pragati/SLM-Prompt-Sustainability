import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Max_Len_Even("This is a test string"), "is")

    def test_no_even_length_words(self):
        self.assertEqual(find_Max_Len_Even("No even length words here"), "-1")

    def test_single_even_length_word(self):
        self.assertEqual(find_Max_Len_Even("Single even length word"), "Single")

    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_string_with_spaces(self):
        self.assertEqual(find_Max_Len_Even("Multiple   words   with   spaces"), "words")

    def test_string_with_special_characters(self):
        self.assertEqual(find_Max_Len_Even("Special!@#characters$%^&*()"), "-1")

    def test_string_with_numbers(self):
        self.assertEqual(find_Max_Len_Even("String with numbers 1234"), "numbers")

    def test_string_with_mixed_case(self):
        self.assertEqual(find_Max_Len_Even("MiXeD cAsE StrInG"), "MiXeD")
