import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sample_nam(['Abc', 'def', 'GHI']), 9)

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_all_capital_letters(self):
        self.assertEqual(sample_nam(['ABC', 'DEF', 'GHI']), 9)

    def test_all_lowercase_letters(self):
        self.assertEqual(sample_nam(['abc', 'def', 'ghi']), 0)

    def test_mixed_case(self):
        self.assertEqual(sample_nam(['Abc', 'def', 'ghI']), 6)

    def test_mixed_case_with_numbers(self):
        self.assertEqual(sample_nam(['Abc1', 'def2', 'ghI3']), 6)

    def test_special_characters(self):
        self.assertEqual(sample_nam(['Abc@', 'def#', 'ghI$']), 0)

    def test_whitespace(self):
        self.assertEqual(sample_nam(['Abc ', ' def', 'ghI']), 6)
