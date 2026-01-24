import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(number_ctr(""), 0)

    def test_single_digit(self):
        self.assertEqual(number_ctr("1"), 1)

    def test_multiple_digits(self):
        self.assertEqual(number_ctr("123"), 3)

    def test_non_digit_characters(self):
        self.assertEqual(number_ctr("abc123"), 3)

    def test_all_digits(self):
        self.assertEqual(number_ctr("1234567890"), 10)

    def test_edge_case_single_character(self):
        self.assertEqual(number_ctr("0"), 1)
        self.assertEqual(number_ctr("9"), 1)

    def test_edge_case_empty_string(self):
        self.assertEqual(number_ctr(""), 0)

    def test_edge_case_single_character_non_digit(self):
        self.assertEqual(number_ctr("a"), 0)
        self.assertEqual(number_ctr("z"), 0)
