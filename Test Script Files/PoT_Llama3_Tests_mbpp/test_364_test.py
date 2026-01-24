import unittest
from mbpp_364_code import min_flip_to_make_string_alternate

class TestMinFlipToMakeStringAlternate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101"), 2)

    def test_edge_case_all_zeros(self):
        self.assertEqual(min_flip_to_make_string_alternate("000000"), 0)

    def test_edge_case_all_ones(self):
        self.assertEqual(min_flip_to_make_string_alternate("111111"), 0)

    def test_edge_case_empty_string(self):
        self.assertEqual(min_flip_to_make_string_alternate(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(min_flip_to_make_string_alternate("0"), 0)

    def test_edge_case_two_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("01"), 1)

    def test_edge_case_three_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("010"), 1)

    def test_edge_case_four_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101"), 2)

    def test_edge_case_five_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("01010"), 2)

    def test_edge_case_six_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101"), 2)

    def test_edge_case_seven_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101010"), 3)

    def test_edge_case_eight_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("01010101"), 3)

    def test_edge_case_nine_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101010"), 4)

    def test_edge_case_ten_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101010101"), 4)

    def test_edge_case_eleven_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("01010101010"), 5)

    def test_edge_case_twelve_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101010101"), 5)

    def test_edge_case_thirteen_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101010101010"), 6)

    def test_edge_case_fourteen_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("01010101010101"), 6)

    def test_edge_case_fifteen_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101010101010"), 7)

    def test_edge_case_sixteen_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101010101010101"), 7)

    def test_edge_case_seventeen_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("01010101010101010"), 8)

    def test_edge_case_eighteen_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("010101010101010101"), 8)

    def test_edge_case_nineteen_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("0101010101010101010"), 9)

    def test_edge_case_twenty_characters(self):
        self.assertEqual(min_flip_to_make_string_alternate("01010101010101010101"), 9)
