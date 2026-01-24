import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToStringAlternate(unittest.TestCase):

    def test_typical_case_with_more_0s(self):
        self.assertEqual(min_flip_to_make_string_alternate('001011100'), 1)

    def test_typical_case_with_more_1s(self):
        self.assertEqual(min_flip_to_make_string_alternate('110100011'), 1)

    def test_typical_case_with_equal_0s_and_1s(self):
        self.assertEqual(min_flip_to_make_string_alternate('0101010101'), 1)

    def test_edge_case_with_all_0s(self):
        self.assertEqual(min_flip_to_make_string_alternate('0000000000'), 0)

    def test_edge_case_with_all_1s(self):
        self.assertEqual(min_flip_to_make_string_alternate('1111111111'), 0)

    def test_edge_case_with_single_character(self):
        self.assertEqual(min_flip_to_make_string_alternate('0'), 0)
        self.assertEqual(min_flip_to_make_string_alternate('1'), 1)

    def test_error_case_with_empty_string(self):
        with self.assertRaises(ValueError):
            min_flip_to_make_string_alternate('')

    def test_error_case_with_non_binary_string(self):
        with self.assertRaises(ValueError):
            min_flip_to_make_string_alternate('2010101010')
