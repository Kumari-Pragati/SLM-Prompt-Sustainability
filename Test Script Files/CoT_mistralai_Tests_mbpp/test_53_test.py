import unittest
from mbpp_53_code import check_Equality

class TestCheckEquality(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(check_Equality(""), "Equal")

    def test_single_character_string(self):
        for char in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(check_Equality(char), "Equal")

    def test_long_string(self):
        long_string = "a" * 100
        self.assertEqual(check_Equality(long_string), "Equal")

    def test_string_with_different_first_and_last_characters(self):
        for char1 in "abcdefghijklmnopqrstuvwxyz":
            for char2 in "abcdefghijklmnopqrstuvwxyz":
                if char1 != char2:
                    test_str = char1 + "a" * 98 + char2
                    self.assertEqual(check_Equality(test_str), "Not Equal")

    def test_string_with_non_string_input(self):
        self.assertRaises(TypeError, check_Equality, 123)
        self.assertRaises(TypeError, check_Equality, [1, 2, 3])
        self.assertRaises(TypeError, check_Equality, (1, 2, 3))
        self.assertRaises(TypeError, check_Equality, None)
        self.assertRaises(TypeError, check_Equality, False)
        self.assertRaises(TypeError, check_Equality, True)
