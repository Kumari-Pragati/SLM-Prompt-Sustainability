import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(length_Of_Last_Word("Hello World"), 5)
        self.assertEqual(length_Of_Last_Word("a"), 1)
        self.assertEqual(length_Of_Last_Word("a "), 1)
        self.assertEqual(length_Of_Last_Word("a b c d"), 1)

    def test_edge_cases(self):
        self.assertEqual(length_Of_Last_Word(""), 0)
        self.assertEqual(length_Of_Last_Word(" "), 0)
        self.assertEqual(length_Of_Last_Word("   "), 0)

    def test_corner_cases(self):
        self.assertEqual(length_Of_Last_Word("   a   b   c   "), 1)
        self.assertEqual(length_Of_Last_Word("   a   b   c   d   "), 1)
        self.assertEqual(length_Of_Last_Word("   a   b   c   d   e   "), 1)
