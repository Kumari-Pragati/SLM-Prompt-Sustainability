import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_capitalize_first_last_letters(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello WOrld")
        self.assertEqual(capitalize_first_last_letters("python is fun"), "Python Is Fun")
        self.assertEqual(capitalize_first_last_letters("a b c d"), "A B C D")
        self.assertEqual(capitalize_first_last_letters(""), "")
        self.assertEqual(capitalize_first_last_letters("123 456"), "123 456")
        self.assertEqual(capitalize_first_last_letters("a b c d e f"), "A B C D E F")
