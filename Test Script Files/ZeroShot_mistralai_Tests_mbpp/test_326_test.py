import unittest
from mbpp_326_code import defaultdict
from thirty_two_six import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(most_occurrences([]), "")

    def test_single_element(self):
        self.assertEqual(most_occurrences(["apple"]), "apple")

    def test_multiple_elements(self):
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "orange", "banana", "banana"]), "banana")

    def test_case_insensitive(self):
        self.assertEqual(most_occurrences(["Apple", "Banana", "Apple", "Orange", "Banana", "Banana"]), "banana")

    def test_multiple_occurrences(self):
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "apple", "orange", "banana", "banana", "banana"]), "banana")

    def test_punctuation(self):
        self.assertEqual(most_occurrences(["apple.", "banana,", "apple", "orange", "banana", "banana"]), "banana")

    def test_numbers(self):
        self.assertEqual(most_occurrences(["apple", "2banana", "apple", "orange", "banana", "banana"]), "banana")
