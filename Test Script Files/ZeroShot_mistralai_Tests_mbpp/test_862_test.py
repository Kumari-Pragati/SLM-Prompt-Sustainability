import unittest
from mbpp_862_code import Counter
import re

def n_common_words(text, n):
    words = re.findall('\w+', text)
    n_common_words = Counter(words).most_common(n)
    return list(n_common_words)

class TestNCommonWords(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(n_common_words("", 1), [])

    def test_single_word(self):
        self.assertEqual(n_common_words("hello", 1), [("hello", 1)])

    def test_multiple_words(self):
        self.assertEqual(n_common_words("hello world hello", 2), [("hello", 2), ("world", 1)])

    def test_case_insensitive(self):
        self.assertEqual(n_common_words("Hello World Hello", 2), [("hello", 2), ("world", 1)])

    def test_multiple_occurrences(self):
        self.assertEqual(n_common_words("aa bb aa cc dd aa", 3), [("aa", 3), ("bb", 1), ("cc", 1), ("dd", 1)])

    def test_long_text(self):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        self.assertEqual(n_common_words(text, 10), [("dolor", 4), ("ipsum", 4), ("et", 3), ("labore", 3), ("consectetur", 2), ("adipiscing", 2), ("elit", 2), ("minim", 2), ("tempor", 2), ("sit", 2)])
