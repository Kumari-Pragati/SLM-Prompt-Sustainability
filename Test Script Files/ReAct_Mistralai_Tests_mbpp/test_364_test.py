import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlip(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(min_flip_to_make_string_alternate(''), 0)

    def test_single_char(self):
        self.assertEqual(min_flip_to_make_string_alternate('0'), 0)
        self.assertEqual(min_flip_to_make_string_alternate('1'), 0)

    def test_alternate_string(self):
        self.assertEqual(min_flip_to_make_string_alternate('010101'), 0)

    def test_all_same_char(self):
        self.assertEqual(min_flip_to_make_string_alternate('000000'), 4)
        self.assertEqual(min_flip_to_make_string_alternate('111111'), 4)

    def test_long_string(self):
        self.assertEqual(min_flip_to_make_string_alternate('010101010101010101010101'), 1)

    def test_single_flip_string(self):
        self.assertEqual(min_flip_to_make_string_alternate('0101010101010101010101'), 1)
