import unittest
from mbpp_172_code import count_occurance

class TestCountOccurance(unittest.TestCase):

    def test_simple_occurance(self):
        self.assertEqual(count_occurance('s td s td'), 2)

    def test_no_occurance(self):
        self.assertEqual(count_occurance('s t d s t d'), 0)

    def test_empty_string(self):
        self.assertEqual(count_occurance(''), 0)

    def test_single_character(self):
        self.assertEqual(count_occurance('s'), 0)

    def test_two_characters(self):
        self.assertEqual(count_occurance('s t'), 0)

    def test_three_characters(self):
        self.assertEqual(count_occurance('s t d'), 1)

    def test_multiple_occurance(self):
        self.assertEqual(count_occurance('s td s td s td'), 3)

    def test_case_sensitivity(self):
        self.assertEqual(count_occurance('S t D'), 0)

    def test_extra_spaces(self):
        self.assertEqual(count_occurance('s  t  d'), 0)

    def test_special_characters(self):
        self.assertEqual(count_occurance('s#t$d'), 0)
