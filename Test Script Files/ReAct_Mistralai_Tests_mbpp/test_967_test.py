import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_accepted_long_vowel_strings(self):
        self.assertEqual(check("AEIOU"), "accepted")
        self.assertEqual(check("aeiou"), "accepted")
        self.assertEqual(check("AeIoU"), "accepted")
        self.assertEqual(check("aEiOu"), "accepted")

    def test_accepted_strings_with_non_vowels(self):
        self.assertEqual(check("A1B2C3"), "not accepted")
        self.assertEqual(check("a1b2c3"), "not accepted")
        self.assertEqual(check("A1B2C3d"), "not accepted")
        self.assertEqual(check("a1b2c3D"), "not accepted")

    def test_accepted_strings_with_repeated_vowels(self):
        self.assertEqual(check("AAAAA"), "accepted")
        self.assertEqual(check("aaaaa"), "accepted")
        self.assertEqual(check("AEIOUAEIOU"), "accepted")
        self.assertEqual(check("aeiouaeiou"), "accepted")

    def test_edge_cases(self):
        self.assertEqual(check("AEIOUAEIOUAEIOU"), "accepted")
        self.assertEqual(check("aeiouaeiouaeiou"), "accepted")
        self.assertEqual(check("AEIOUAEIOU1"), "not accepted")
        self.assertEqual(check("aeiouaeiou1"), "not accepted")

    def test_error_cases(self):
        self.assertRaises(TypeError, check, 123)
        self.assertRaises(TypeError, check, [])
        self.assertRaises(TypeError, check, ())
        self.assertRaises(TypeError, check, None)
