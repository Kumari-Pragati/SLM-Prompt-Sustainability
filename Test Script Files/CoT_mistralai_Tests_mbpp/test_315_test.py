import unittest
from mbpp_315_code import find_Max_Len_Even

class TestFindMaxLenEven(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_Max_Len_Even(""), "-1")

    def test_single_word(self):
        for word in ["hello", "world", "Python", "unittest"]:
            self.assertEqual(find_Max_Len_Even(word), word)

    def test_multiple_words(self):
        for words in ["hello world", "Python unittest", "315 code test"]:
            self.assertEqual(find_Max_Len_Even(words), words.split()[0])

    def test_odd_length(self):
        self.assertEqual(find_Max_Len_Even("abc"), "-1")
        self.assertEqual(find_Max_Len_Even("a b c"), "-1")
        self.assertEqual(find_Max_Len_Even("a b c d"), "a b c")

    def test_leading_space(self):
        self.assertEqual(find_Max_Len_Even(" a word"), "word")
        self.assertEqual(find_Max_Len_Even(" a   word"), "word")

    def test_trailing_space(self):
        self.assertEqual(find_Max_Len_Even("word "), "word")
        self.assertEqual(find_Max_Len_Even("word   "), "word")

    def test_multiple_spaces(self):
        self.assertEqual(find_Max_Len_Even("word1 word2 word3"), "word1")
        self.assertEqual(find_Max_Len_Even("word1   word2   word3"), "word1")

    def test_punctuation(self):
        self.assertEqual(find_Max_Len_Even("hello, world!"), "hello")
        self.assertEqual(find_Max_Len_Even("Python-unittest"), "Python")
        self.assertEqual(find_Max_Len_Even("315 code test."), "315")

    def test_special_characters(self):
        self.assertEqual(find_Max_Len_Even("!@#$%^&*()_+-=[]{}|;:'\",.<>/?Hello World"), "!@#$%^&*()_+-=[]{}|;:'\",.<>/")
        self.assertEqual(find_Max_Len_Even("Hello_World"), "Hello")
