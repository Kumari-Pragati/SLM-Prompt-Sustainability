import unittest
from967_code import check

class TestCheckFunction(unittest.TestCase):
    def test_accepted_string(self):
        self.assertEqual(check("aeiou"), "accepted")
        self.assertEqual(check("AeIou"), "accepted")
        self.assertEqual(check("AeiouX"), "accepted")
        self.assertEqual(check("aEiOu"), "accepted")

    def test_not_accepted_string(self):
        self.assertEqual(check("abcde"), "not accepted")
        self.assertEqual(check("AbCDe"), "not accepted")
        self.assertEqual(check("AbCdE"), "not accepted")
        self.assertEqual(check("AeIouX"), "not accepted")

    def test_empty_string(self):
        self.assertEqual(check(""), "not accepted")

    def test_single_letter(self):
        for char in "QWERTYUIOPASDFGZXCVBNMqwertyuiopasdfgzxcvbnm":
            self.assertEqual(check(char), "not accepted")
