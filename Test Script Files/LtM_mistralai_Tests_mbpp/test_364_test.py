import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):

    def test_simple_alternate(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("1010"), 0)

    def test_simple_non_alternate(self):
        self.assertEqual(min_flip_to_make_string_alternate("0000"), 4)
        self.assertEqual(min_flip_to_make_string_alternate("1111"), 4)

    def test_edge_cases(self):
        self.assertEqual(min_flip_to_make_string_alternate("0"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("1"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("01"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("10"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("010"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("101"), 1)

    def test_boundary_cases(self):
        self.assertEqual(min_flip_to_make_string_alternate("000000000"), 8)
        self.assertEqual(min_flip_to_make_string_alternate("111111111"), 8)
        self.assertEqual(min_flip_to_make_string_alternate("010101010101"), 2)
        self.assertEqual(min_flip_to_make_string_alternate("101010101010"), 2)
