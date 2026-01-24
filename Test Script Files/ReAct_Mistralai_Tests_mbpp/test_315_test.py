import unittest
from315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_single_character(self):
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEqual(find_Max_Len_Even(char), "-1")

    def test_single_word(self):
        for word in ["hello", "world", "Python", "unittest"]:
            self.assertEqual(find_Max_Len_Even(word), word)

    def test_multiple_words(self):
        for words in ["hello world", "Python unittest", "3 5 7 9"]:
            self.assertEqual(find_Max_Len_Even(words), "3 5" if words.count(" ") == 2 else words.split(" ")[1])

    def test_leading_and_trailing_spaces(self):
        for words in [" hello world ", " 3 5 7 9 "]:
            self.assertEqual(find_Max_Len_Even(words), "hello world" if words.count(" ") == 2 else "3 5")

    def test_odd_length_string(self):
        for words in ["hello world!", "Python unittest#", "3 5 7 9&"]:
            self.assertEqual(find_Max_Len_Even(words), "-1")

    def test_only_spaces(self):
        self.assertEqual(find_Max_Len_Even("   "), "-1")
