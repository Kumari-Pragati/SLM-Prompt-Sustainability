import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_accepted(self):
        self.assertEqual(check("aeiouAEIOU"), 'accepted')

    def test_not_accepted(self):
        self.assertEqual(check("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), 'not accepted')

    def test_edge_case(self):
        self.assertEqual(check("AEIOUaeiou"), 'accepted')

    def test_empty_string(self):
        self.assertEqual(check(""), 'not accepted')

    def test_single_character(self):
        self.assertEqual(check("a"), 'not accepted')

    def test_multiple_characters(self):
        self.assertEqual(check("abc"), 'not accepted')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            check(123)

    def test_mixed_case(self):
        self.assertEqual(check("AEIOUaeiou"), 'accepted')
