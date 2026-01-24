import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_same_strings(self):
        self.assertEqual(min_Swaps("abc", "abc"), 0)

    def test_identical_strings(self):
        self.assertEqual(min_Swaps("aabb", "aabb"), 0)

    def test_alternating_strings(self):
        self.assertEqual(min_Swaps("abcd", "cdab"), 1)

    def test_longer_string_with_matching_prefix(self):
        self.assertEqual(min_Swaps("abcd", "cd"), 2)

    def test_longer_string_with_matching_suffix(self):
        self.assertEqual(min_Swaps("abcd", "ab"), 2)

    def test_longer_string_with_no_match(self):
        self.assertEqual(min_Swaps("abcd", "efgh"), 4)

    def test_empty_strings(self):
        self.assertEqual(min_Swaps("", ""), 0)

    def test_single_character_strings(self):
        self.assertEqual(min_Swaps("a", "b"), 1)

    def test_single_character_strings_same(self):
        self.assertEqual(min_Swaps("a", "a"), 0)

    def test_invalid_input_empty_string1(self):
        with self.assertRaises(ValueError):
            min_Swaps("", "")

    def test_invalid_input_empty_string2(self):
        with self.assertRaises(ValueError):
            min_Swaps("", None)

    def test_invalid_input_none(self):
        with self.assertRaises(ValueError):
            min_Swaps(None, "abc")
