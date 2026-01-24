import unittest
from mbpp_773_code import occurance_substring

class TestOccuranceSubstring(unittest.TestCase):

    def test_occurance_substring(self):
        self.assertEqual(occurance_substring('Hello, world!', 'world'), ('world', 7, 12))
        self.assertEqual(occurance_substring('This is a test string', 'test'), ('test', 10, 14))
        self.assertEqual(occurance_substring('Python is fun', 'fun'), ('fun', 10, 13))
        self.assertEqual(occurance_substring('No match here', 'nonexistent'), None)
