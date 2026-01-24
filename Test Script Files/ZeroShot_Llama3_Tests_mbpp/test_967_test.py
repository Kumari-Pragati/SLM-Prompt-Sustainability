import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_accepted(self):
        self.assertEqual(check("aeiouAEIOU"), 'accepted')

    def test_not_accepted(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), 'not accepted')

    def test_accepted_with_spaces(self):
        self.assertEqual(check("aeiouAEIOU  "), 'accepted')

    def test_not_accepted_with_spaces(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ "), 'not accepted')

    def test_accepted_with_punctuation(self):
        self.assertEqual(check("aeiouAEIOU!"), 'accepted')

    def test_not_accepted_with_punctuation(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ!"), 'not accepted')

    def test_accepted_with_numbers(self):
        self.assertEqual(check("aeiouAEIOU123"), 'accepted')

    def test_not_accepted_with_numbers(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ123"), 'not accepted')

    def test_empty_string(self):
        self.assertEqual(check(""), 'not accepted')

    def test_single_character(self):
        self.assertEqual(check("a"), 'not accepted')

    def test_multiple_characters(self):
        self.assertEqual(check("abc"), 'not accepted')
