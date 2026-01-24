import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(rearange_string("a"), "a")

    def test_two_character_string(self):
        self.assertEqual(rearange_string("aa"), "aa")

    def test_three_character_string(self):
        self.assertEqual(rearange_string("aab"), "aab")

    def test_four_character_string(self):
        self.assertEqual(rearange_string("aabbc"), "aabbc")

    def test_five_character_string(self):
        self.assertEqual(rearange_string("aabbcde"), "aabbcde")

    def test_long_string(self):
        self.assertEqual(rearange_string("aabbcdeffgh"), "aabbcdeffgh")

    def test_string_with_no_repeats(self):
        self.assertEqual(rearange_string("abcdef"), "abcdef")

    def test_string_with_no_repeats_and_length_greater_than_or_equal_to_5(self):
        self.assertEqual(rearange_string("abcdefg"), "abcdefg")

    def test_string_with_repeats_and_length_greater_than_or_equal_to_5(self):
        self.assertEqual(rearange_string("aabbcdeffgh"), "aabbcdeffgh")

    def test_string_with_repeats_and_length_greater_than_or_equal_to_10(self):
        self.assertEqual(rearange_string("aabbcdeffghijkl"), "aabbcdeffghijkl")

    def test_string_with_repeats_and_length_greater_than_or_equal_to_15(self):
        self.assertEqual(rearange_string("aabbcdeffghijklmnop"), "aabbcdeffghijklmnop")

    def test_string_with_repeats_and_length_greater_than_or_equal_to_20(self):
        self.assertEqual(rearange_string("aabbcdeffghijklmnopqrstuvwxyz"), "aabbcdeffghijklmnopqrstuvwxyz")
