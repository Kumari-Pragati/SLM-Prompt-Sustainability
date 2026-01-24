import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):
    def test_simple_equal(self):
        self.assertEqual(check_Equality("hello"), "Equal")

    def test_simple_not_equal(self):
        self.assertEqual(check_Equality("hello world"), "Not Equal")

    def test_empty_string(self):
        self.assertEqual(check_Equality(""), "Not Equal")

    def test_single_character(self):
        self.assertEqual(check_Equality("a"), "Equal")

    def test_long_string(self):
        self.assertEqual(check_Equality("hello world hello"), "Equal")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            check_Equality(123)
