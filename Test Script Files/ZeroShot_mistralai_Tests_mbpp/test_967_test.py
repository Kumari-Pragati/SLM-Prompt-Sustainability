import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_accepted_string(self):
        self.assertEqual(check("aeiou"), "accepted")
        self.assertEqual(check("AeIou"), "accepted")
        self.assertEqual(check("AeIouX"), "accepted")
        self.assertEqual(check("AeIouXy"), "not accepted")

    def test_not_accepted_string(self):
        self.assertEqual(check("abcde"), "not accepted")
        self.assertEqual(check("AbCdE"), "not accepted")
        self.assertEqual(check("AbCdEx"), "not accepted")
        self.assertEqual(check("AbCdExy"), "not accepted")
