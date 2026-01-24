import unittest
from mbpp_495_code import remove_lowercase

class TestRemoveLowercase(unittest.TestCase):

    def test_empty_string(self):
        """Test if an empty string is correctly processed."""
        self.assertEqual(remove_lowercase(""), "")

    def test_single_uppercase_letter(self):
        """Test if a single uppercase letter is correctly processed."""
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.assertEqual(remove_lowercase(char), char.upper())

    def test_single_uppercase_word(self):
        """Test if a single uppercase word is correctly processed."""
        for word in ["HELLO", "WORLD", "PYTHON"]:
            self.assertEqual(remove_lowercase(word), word.upper())

    def test_multiple_uppercase_words(self):
        """Test if multiple uppercase words are correctly processed."""
        for word in ["HELLO WORLD", "PYTHON UNITTEST", "REACT STYLE LOOP"]:
            self.assertEqual(remove_lowercase(word), word.upper().replace(" ", ""))

    def test_mixed_case_word(self):
        """Test if a mixed case word is correctly processed."""
        for word in ["HelloWorld", "PythonUnittest", "ReactStyleLoop"]:
            self.assertEqual(remove_lowercase(word), word.upper().replace(" ", ""))

    def test_mixed_case_sentence(self):
        """Test if a mixed case sentence is correctly processed."""
        for sentence in ["Hello World!", "Python Unittest is fun!", "React Style Loop is powerful!"]:
            self.assertEqual(remove_lowercase(sentence), sentence.upper().replace(" ", ""))

    def test_punctuation_and_numbers(self):
        """Test if punctuation and numbers are correctly processed."""
        for sentence in ["Hello, World! 123", "Python 456 Unittest is fun!", "React Style Loop!@#$%^&*()"]:
            self.assertEqual(remove_lowercase(sentence), sentence.upper().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace(" ", ""))

    def test_multiple_spaces(self):
        """Test if multiple spaces are correctly processed."""
        for sentence in [" Hello World  ", " Python   Unittest  "]:
            self.assertEqual(remove_lowercase(sentence), sentence.upper().replace(" ", ""))

    def test_leading_trailing_spaces(self):
        """Test if leading and trailing spaces are correctly processed."""
        for sentence in [" Hello World ", " Python   Unittest  ", "   React Style Loop   "]:
            self.assertEqual(remove_lowercase(sentence), sentence.upper().replace(" ", ""))

    def test_empty_list(self):
        """Test if an empty list is correctly processed."""
        self.assertEqual(remove_lowercase([]), [])

    def test_single_element_list(self):
        """Test if a single element list is correctly processed."""
        for element in ["Hello", "World", "Python"]:
            self.assertEqual(remove_lowercase([element]), [element.upper()])

    def test_multiple_element_list(self):
        """Test if a multiple element list is correctly processed."""
        for elements in [["Hello", "World"], ["Python", "Unittest"], ["React", "Style", "Loop"]]:
            self.assertEqual(remove_lowercase(elements), [elements[0].upper(), elements[1].upper(), elements[2].upper()])
