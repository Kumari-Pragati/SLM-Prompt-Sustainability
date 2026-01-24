import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("101010"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("000000"), 2)
        self.assertEqual(min_flip_to_make_string_alternate("111111"), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_flip_to_make_string_alternate(""), 0)
        self.assertEqual(min_flip_to_make_string_alternate("0"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("1"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("01"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("10"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("00101"), 2)
        self.assertEqual(min_flip_to_make_string_alternate("10010"), 2)

    def test_special_cases(self):
        self.assertEqual(min_flip_to_make_string_alternate("0000000000"), 4)
        self.assertEqual(min_flip_to_make_string_alternate("1111111111"), 4)
        self.assertEqual(min_flip_to_make_string_alternate("0101010101"), 2)
        self.assertEqual(min_flip_to_make_string_alternate("1010101010"), 2)
