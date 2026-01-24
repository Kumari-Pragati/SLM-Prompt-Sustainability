import unittest
from mbpp_674_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_duplicate("a b a c d e"), "a b c d e")
        self.assertEqual(remove_duplicate("a"), "a")
        self.assertEqual(remove_duplicate(""), "")

    def test_edge_cases(self):
        self.assertEqual(remove_duplicate("a a"), "a")
        self.assertEqual(remove_duplicate("a b a b"), "a b")
        self.assertEqual(remove_duplicate("a\nb"), "a\nb")
        self.assertEqual(remove_duplicate("a\nb\na"), "a\nb")

    def test_complex(self):
        self.assertEqual(remove_duplicate("a a b b c c d d"), "a b c d")
        self.assertEqual(remove_duplicate("a\nb\nc\nd\na\nb\nc\nd"), "a\nb\nc\nd")
        self.assertEqual(remove_duplicate("a\nb\nc\nd\na\nb\nc\nd\na\nb\nc\nd"), "a\nb\nc\nd")
