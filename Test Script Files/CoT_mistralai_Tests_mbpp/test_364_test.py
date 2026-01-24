import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(min_flip_to_make_string_alternate(''), 0)

    def test_single_character(self):
        self.assertEqual(min_flip_to_make_string_alternate('0'), 0)
        self.assertEqual(min_flip_to_make_string_alternate('1'), 0)

    def test_alternate_string(self):
        self.assertEqual(min_flip_to_make_string_alternate('010101'), 0)

    def test_non_alternate_string(self):
        self.assertEqual(min_flip_to_make_string_alternate('000000'), 3)
        self.assertEqual(min_flip_to_make_string_alternate('111111'), 3)

    def test_long_string(self):
        self.assertEqual(min_flip_to_make_string_alternate('010101010101010101010101'), 1)

    def test_all_zeroes(self):
        self.assertEqual(min_flip_to_make_string_alternate('00000000000000000000000000000000'), 32)

    def test_all_ones(self):
        self.assertEqual(min_flip_to_make_string_alternate('11111111111111111111111111111111'), 32)

    def test_mixed_case(self):
        self.assertEqual(min_flip_to_make_string_alternate('01010101010101010101010101'), 1)
