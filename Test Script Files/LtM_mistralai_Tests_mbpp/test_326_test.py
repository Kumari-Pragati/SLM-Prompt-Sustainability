import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]), "apple")
        self.assertEqual(most_occurrences(["orange", "banana", "orange", "orange", "banana"]), "orange")
        self.assertEqual(most_occurrences(["apple", "banana", "orange", "apple", "banana", "banana"]), "banana")

    def test_edge_cases(self):
        self.assertEqual(most_occurrences([]), None)
        self.assertEqual(most_occurrences([""]), None)
        self.assertEqual(most_occurrences(["a", "a", "b", "a", "b", "a"]), "a")
        self.assertEqual(most_occurrences(["a", "b", "a", "b", "a", "c"]), "a")
        self.assertEqual(most_occurrences(["a", "b", "a", "b", "a", "b"]), "b")

    def test_complex(self):
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "orange", "banana", "apple", "orange", "banana", "apple"]), "apple")
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "orange", "banana", "apple", "orange", "banana", "apple", "orange"]), "orange")
        self.assertEqual(most_occurrences(["apple", "banana", "apple", "orange", "banana", "apple", "orange", "banana", "apple", "orange", "banana"]), "banana")
