import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):

    def test_min_flip_to_make_string_alternate(self):
        self.assertEqual(min_flip_to_make_string_alternate('1101'), 1)
        self.assertEqual(min_flip_to_make_string_alternate('111000'), 0)
        self.assertEqual(min_flip_to_make_string_alternate('111111'), 2)
        self.assertEqual(min_flip_to_make_string_alternate('000000'), 2)
        self.assertEqual(min_flip_to_make_string_alternate('1010101010'), 1)
        self.assertEqual(min_flip_to_make_string_alternate('0101010101'), 1)
        self.assertEqual(min_flip_to_make_string_alternate(''), 0)
