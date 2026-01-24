import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rearange_string("aab"), "aba")

    def test_empty_string(self):
        self.assertEqual(rearange_string(""), "")

    def test_single_character_string(self):
        self.assertEqual(rearange_string("a"), "a")

    def test_string_with_same_characters(self):
        self.assertEqual(rearange_string("aaa"), "aaa")

    def test_string_with_different_characters(self):
        self.assertEqual(rearange_string("abc"), "abc")

    def test_string_with_more_than_two_most_frequent_characters(self):
        self.assertEqual(rearange_string("aabbcc"), "abcabc")

    def test_string_with_two_most_frequent_characters(self):
        self.assertEqual(rearange_string("aabbc"), "ababc")

    def test_string_with_less_than_two_most_frequent_characters(self):
        self.assertEqual(rearange_string("abbc"), "abc")

    def test_string_with_equal_number_of_characters(self):
        self.assertEqual(rearange_string("aabbccdd"), "abcdabcd")

    def test_string_with_more_than_equal_number_of_characters(self):
        self.assertEqual(rearange_string("aabbccdde"), "abcdeabcde")

    def test_string_with_less_than_equal_number_of_characters(self):
        self.assertEqual(rearange_string("aabbccdd"), "abcdabcd")

    def test_string_with_most_frequent_characters_more_than_half(self):
        self.assertEqual(rearange_string("aabbccddeeff"), "abcdefabcdef")

    def test_string_with_most_frequent_characters_less_than_half(self):
        self.assertEqual(rearange_string("aabbccddeeffg"), "abcdefgabcdefg")

    def test_string_with_most_frequent_characters_equal_to_half(self):
        self.assertEqual(rearange_string("aabbccddeeffgg"), "abcdefgabcdefg")

    def test_string_with_most_frequent_characters_more_than_twice_most_frequent(self):
        self.assertEqual(rearange_string("aabbccddeeffgghh"), "abcdefghabcdefgh")

    def test_string_with_most_frequent_characters_less_than_twice_most_frequent(self):
        self.assertEqual(rearange_string("aabbccddeeffgghhii"), "abcdefghiabcdefghi")

    def test_string_with_most_frequent_characters_equal_to_twice_most_frequent(self):
        self.assertEqual(rearange_string("aabbccddeeffgghhii"), "abcdefghiabcdefghi")

    def test_string_with_most_frequent_characters_more_than_twice_most_frequent_and_more_than_half(self):
        self.assertEqual(rearange_string("aabbccddeeffgghhiijj"), "abcdefghijabcdefghij")

    def test_string_with_most_frequent_characters_less_than_twice_most_frequent_and_less_than_half(self):
        self.assertEqual(rearange_string("aabbccddeeffgghh"), "abcdefghabcdefgh")

    def test_string_with_most_frequent_characters_equal_to_twice_most_frequent_and_equal_to_half(self):
        self.assertEqual(rearange_string("aabbccddeeffgghh"), "abcdefghabcdefgh")
