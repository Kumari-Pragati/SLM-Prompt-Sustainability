import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_flip_to_make_string_alternate('10101'), 1)

    def test_all_same_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate('11111'), 0)

    def test_all_different_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate('010101010101'), 1)

    def test_empty_string(self):
        self.assertEqual(min_flip_to_make_string_alternate(''), 0)

    def test_single_character(self):
        self.assertEqual(min_flip_to_make_string_alternate('0'), 0)
        self.assertEqual(min_flip_to_make_string_alternate('1'), 0)

    def test_long_string(self):
        self.assertEqual(min_flip_to_make_string_alternate('0' * 1000 + '1'), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_flip_to_make_string_alternate(12345)
        with self.assertRaises(TypeError):
            min_flip_to_make_string_alternate(['1', '0', '1', '0', '1'])
