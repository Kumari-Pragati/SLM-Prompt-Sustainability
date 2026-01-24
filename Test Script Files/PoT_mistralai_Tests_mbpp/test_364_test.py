import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(min_flip_to_make_string_alternate("001010"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("101010"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("010101"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("111111"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("0"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("1"), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(min_flip_to_make_string_alternate(""), 0)
        self.assertEqual(min_flip_to_make_string_alternate("00"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("11"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("01101"), 2)
        self.assertEqual(min_flip_to_make_string_alternate("10110"), 2)
