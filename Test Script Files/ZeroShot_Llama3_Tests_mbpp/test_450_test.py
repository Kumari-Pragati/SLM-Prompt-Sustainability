import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_extract_string(self):
        self.assertEqual(extract_string("hello", 2), ["he", "el", "ll", "lo"])
        self.assertEqual(extract_string("hello", 3), ["hel", "ell", "llo"])
        self.assertEqual(extract_string("hello", 4), ["hell", "llo"])
        self.assertEqual(extract_string("hello", 5), ["hello"])
        self.assertEqual(extract_string("hello", 6), [])
        self.assertEqual(extract_string("123456", 1), ["1", "2", "3", "4", "5", "6"])
        self.assertEqual(extract_string("123456", 2), ["12", "23", "34", "45", "56"])
        self.assertEqual(extract_string("123456", 3), ["123", "234", "345", "456"])
        self.assertEqual(extract_string("123456", 4), ["1234", "2345", "3456"])
        self.assertEqual(extract_string("123456", 5), ["12345", "23456"])
        self.assertEqual(extract_string("123456", 6), ["123456"])
        self.assertEqual(extract_string("123456", 7), [])
