import unittest
from mbpp_131_code import reverse_vowels

class TestReverseVowels(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(reverse_vowels("hello"), "holle")

    def test_edge_case_with_no_vowels(self):
        self.assertEqual(reverse_vowels("rhythm"), "rhythm")

    def test_boundary_case_with_single_vowel(self):
        self.assertEqual(reverse_vowels("a"), "a")

    def test_corner_case_with_duplicate_vowels(self):
        self.assertEqual(reverse_vowels("beautiful"), "beautiful")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            reverse_vowels(123)
