import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):
    def test_alternate_string(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101"), 0)

    def test_all_zeroes(self):
        self.assertEqual(min_flip_to_make_string_alternate("000000"), 0)

    def test_all_ones(self):
        self.assertEqual(min_flip_to_make_string_alternate("111111"), 0)

    def test_single_character(self):
        self.assertEqual(min_flip_to_make_string_alternate("0"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("1"), 1)

    def test_empty_string(self):
        self.assertEqual(min_flip_to_make_string_alternate(""), 0)
