import unittest
from mbpp_374_code import permute_string

class TestPermuteString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(permute_string(''), [''])

    def test_single_character_string(self):
        self.assertEqual(permute_string('a'), ['a'])

    def test_multiple_characters_string(self):
        self.assertEqual(permute_string('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_repeated_characters_string(self):
        self.assertEqual(permute_string('aaa'), ['aaa', 'aaa', 'aia', 'iaa'])

    def test_edge_case_long_string(self):
        long_str = 'a' * 100
        self.assertEqual(len(permute_string(long_str)), 101 * 100)

    def test_edge_case_short_string(self):
        short_str = 'a'
        self.assertEqual(permute_string(short_str), ['a'])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            permute_string(123)
