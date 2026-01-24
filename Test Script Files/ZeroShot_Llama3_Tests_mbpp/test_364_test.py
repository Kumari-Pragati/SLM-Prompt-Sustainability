import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(min_flip_to_make_string_alternate(""), 0)

    def test_single_character(self):
        self.assertEqual(min_flip_to_make_string_alternate("0"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("1"), 0)

    def test_alternating_string(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101"), 0)

    def test_non_alternating_string(self):
        self.assertEqual(min_flip_to_make_string_alternate("111111"), 6)
        self.assertEqual(min_flip_to_make_string_alternate("000000"), 0)

    def test_mixed_string(self):
        self.assertEqual(min_flip_to_make_string_alternate("101010"), 2)

    def test_long_string(self):
        self.assertEqual(min_flip_to_make_string_alternate("1111111111111111"), 12)
        self.assertEqual(min_flip_to_make_string_alternate("0000000000000000"), 0)
