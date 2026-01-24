import unittest
from mbpp_862_code import Counter
import re

def n_common_words(text,n):
  words = re.findall('\w+',text)
  n_common_words= Counter(words).most_common(n)
  return list(n_common_words)

class TestNCommonWords(unittest.TestCase):

    def test_n_common_words(self):
        text = "hello world hello python python world"
        n = 2
        expected_output = [('world', 2), ('hello', 2), ('python', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_n_common_words_with_less_words(self):
        text = "hello world hello python python world"
        n = 4
        expected_output = [('world', 2), ('hello', 2), ('python', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_n_common_words_with_more_words(self):
        text = "hello world hello python python world java java"
        n = 3
        expected_output = [('world', 2), ('hello', 2), ('python', 2), ('java', 2)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_n_common_words_with_same_words(self):
        text = "hello hello hello hello hello"
        n = 1
        expected_output = [('hello', 5)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_n_common_words_with_empty_text(self):
        text = ""
        n = 1
        expected_output = []
        self.assertEqual(n_common_words(text, n), expected_output)
