import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sample_nam(['Name', 'nAmE', 'NaMe']), 5)

    def test_single_capital_letter(self):
        self.assertEqual(sample_nam(['N']), 1)

    def test_all_capital_letters(self):
        self.assertEqual(sample_nam(['NAME', 'NAMES']), 4)

    def test_all_lowercase_letters(self):
        self.assertEqual(sample_nam(['name', 'names']), 0)

    def test_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_mixed_case_letters(self):
        self.assertEqual(sample_nam(['nAmE', 'NaMe']), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sample_nam(123)
