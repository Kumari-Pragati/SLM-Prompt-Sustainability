import unittest
from mbpp_699_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_same_strings(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)

    def test_different_length_strings(self):
        self.assertEqual(min_Swaps('abc', 'abcd'), "Not Possible")

    def test_strings_with_same_characters_different_positions(self):
        self.assertEqual(min_Swaps('abc', 'acb'), 1)

    def test_strings_with_different_characters(self):
        self.assertEqual(min_Swaps('abc', 'def'), "Not Possible")

    def test_strings_with_same_characters_different_counts(self):
        self.assertEqual(min_Swaps('aabb', 'abab'), 1)

    def test_strings_with_same_characters_different_counts_2(self):
        self.assertEqual(min_Swaps('aabbcc', 'abcabc'), 2)
