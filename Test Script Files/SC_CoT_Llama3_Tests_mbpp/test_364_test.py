import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101"), 2)
        self.assertEqual(min_flip_to_make_string_alternate("1010"), 2)
        self.assertEqual(min_flip_to_make_string_alternate("1111"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("0000"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("101010"), 4)

    def test_edge_cases(self):
        self.assertEqual(min_flip_to_make_string_alternate(""), 0)
        self.assertEqual(min_flip_to_make_string_alternate("1"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("0"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("11"), 0)
        self.assertEqual(min_flip_to_make_string_alternate("00"), 0)

    def test_special_cases(self):
        self.assertEqual(min_flip_to_make_string_alternate("111"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("000"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("101"), 1)
        self.assertEqual(min_flip_to_make_string_alternate("010"), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_flip_to_make_string_alternate(None)
        with self.assertRaises(TypeError):
            min_flip_to_make_string_alternate("")
