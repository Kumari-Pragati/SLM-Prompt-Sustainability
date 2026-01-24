import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_only_zeroes(self):
        self.assertEqual(check('0000000'), 'Yes')

    def test_only_ones(self):
        self.assertEqual(check('1111111'), 'Yes')

    def test_mixed_ones_and_zeroes(self):
        self.assertEqual(check('1010101'), 'Yes')

    def test_empty_string(self):
        self.assertEqual(check(''), 'Yes')

    def test_string_with_other_characters(self):
        self.assertEqual(check('1010101a'), 'No')

    def test_string_with_only_one_character(self):
        self.assertEqual(check('1'), 'Yes')

    def test_string_with_only_zero(self):
        self.assertEqual(check('0'), 'Yes')

    def test_string_with_only_one(self):
        self.assertEqual(check('1'), 'Yes')
