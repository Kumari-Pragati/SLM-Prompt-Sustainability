import unittest
from mbpp_967_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case_accepted(self):
        self.assertEqual(check('aeiou'), 'accepted')

    def test_typical_case_not_accepted(self):
        self.assertEqual(check('bcdfghjklmnpqrstvwxyz'), 'not accepted')

    def test_edge_case_five_vowels(self):
        self.assertEqual(check('aeiouy'), 'accepted')

    def test_edge_case_no_vowels(self):
        self.assertEqual(check('bcdfghjklmnpqrstvwxyz1234567890'), 'not accepted')

    def test_edge_case_empty_string(self):
        self.assertEqual(check(''), 'not accepted')

    def test_explicitly_handled_error_case_none_input(self):
        with self.assertRaises(TypeError):
            check(None)

    def test_explicitly_handled_error_case_integer_input(self):
        with self.assertRaises(TypeError):
            check(12345)

    def test_explicitly_handled_error_case_float_input(self):
        with self.assertRaises(TypeError):
            check(123.45)
