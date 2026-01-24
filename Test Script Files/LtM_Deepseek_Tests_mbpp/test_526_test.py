import unittest
from mbpp_526_code import capitalize_first_last_letters

class TestCapitalizeFirstLastLetters(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(capitalize_first_last_letters("hello world"), "Hello World")
        self.assertEqual(capitalize_first_last_letters("python is fun"), "Python Is Fun")

    def test_edge_conditions(self):
        self.assertEqual(capitalize_first_last_letters(""), "")
        self.assertEqual(capitalize_first_last_letters("a"), "A")
        self.assertEqual(capitalize_first_last_letters("12345"), "12345")

    def test_complex_cases(self):
        self.assertEqual(capitalize_first_last_letters("the quick brown fox"), "The Quick Brown Fox")
        self.assertEqual(capitalize_first_last_letters("jumps over the lazy dog"), "Jumps Over The Lazy Dog")
