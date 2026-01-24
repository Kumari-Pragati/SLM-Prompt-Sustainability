import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(most_occurrences([]), "")

    def test_single_element(self):
        self.assertEqual(most_occurrences(["apple"]), "apple")

    def test_multiple_elements_same_word(self):
        self.assertEqual(most_occurrences(["apple", "apple", "banana"]), "apple")

    def test_multiple_elements_different_words(self):
        self.assertEqual(most_occurrences(["apple", "banana", "apple"]), "apple")

    def test_case_sensitivity(self):
        self.assertEqual(most_occurrences(["Apple", "apple"]), "Apple")

    def test_multiple_occurrences_same_word(self):
        self.assertEqual(most_occurrences(["apple", "apple", "banana", "apple", "banana", "apple"]), "apple")

    def test_no_occurrences(self):
        self.assertEqual(most_occurrences(["banana", "orange", "kiwi"]), "")

    def test_whitespace(self):
        self.assertEqual(most_occurrences(["apple apple", "banana"]), "apple")

    def test_punctuation(self):
        self.assertEqual(most_occurrences(["apple.", "banana!", "apple"]), "apple")

    def test_numbers(self):
        self.assertEqual(most_occurrences(["apple", "2", "banana"]), "apple")

    def test_error_empty_word(self):
        with self.assertRaises(ValueError):
            most_occurrences([""])

    def test_error_non_string_element(self):
        with self.assertRaises(TypeError):
            most_occurrences([1, 2, 3])
