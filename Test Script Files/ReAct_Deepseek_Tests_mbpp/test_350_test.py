import unittest
from mbpp_350_code import minimum_Length

class TestMinimumLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(minimum_Length('aabbbccc'), 0)

    def test_edge_case_single_char(self):
        self.assertEqual(minimum_Length('a'), 1)

    def test_edge_case_same_chars(self):
        self.assertEqual(minimum_Length('aaaaa'), 5)

    def test_edge_case_empty_string(self):
        self.assertEqual(minimum_Length(''), 0)

    def test_typical_case_with_spaces(self):
        self.assertEqual(minimum_Length('a b c'), 0)

    def test_typical_case_with_numbers(self):
        self.assertEqual(minimum_Length('1234567890'), 10)

    def test_typical_case_with_mixed_chars(self):
        self.assertEqual(minimum_Length('abc123def'), 0)

    def test_edge_case_lowercase_uppercase(self):
        self.assertEqual(minimum_Length('aA'), 1)

    def test_edge_case_special_chars(self):
        self.assertEqual(minimum_Length('!@#$%^&*()'), 10)

    def test_typical_case_with_repetition(self):
        self.assertEqual(minimum_Length('aabbcc'), 0)

    def test_edge_case_max_occurence(self):
        self.assertEqual(minimum_Length('aaaaaaaaaaaaaaaaaaaa'), 25)
