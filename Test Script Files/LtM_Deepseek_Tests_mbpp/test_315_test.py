import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_simple_even_length_string(self):
        self.assertEqual(find_Max_Len_Even("Hello World"), "Hello")

    def test_complex_even_length_string(self):
        self.assertEqual(find_Max_Len_Even("This is a test string"), "is a")

    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_string_with_single_word(self):
        self.assertEqual(find_Max_Len_Even("Python"), "-1")

    def test_string_with_odd_length(self):
        self.assertEqual(find_Max_Len_Even("This is a test string with odd length"), "is a")

    def test_string_with_even_length(self):
        self.assertEqual(find_Max_Len_Even("This is a test string with even length"), "is a test")
