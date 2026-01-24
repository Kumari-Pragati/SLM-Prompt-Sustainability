import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(length_Of_Last_Word("hello world"), 5)
        self.assertEqual(length_Of_Last_Word("hello world "), 5)
        self.assertEqual(length_Of_Last_Word("hello world   "), 5)

    def test_edge_cases(self):
        self.assertEqual(length_Of_Last_Word(""), 0)
        self.assertEqual(length_Of_Last_Word(" "), 0)
        self.assertEqual(length_Of_Last_Word("hello"), 5)
        self.assertEqual(length_Of_Last_Word("hello\t"), 5)
        self.assertEqual(length_Of_Last_Word("\thello"), 4)
