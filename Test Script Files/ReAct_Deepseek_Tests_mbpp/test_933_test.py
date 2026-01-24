import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('single'), 'single')

    def test_all_caps(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'allcaps')

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake('MiXeDcAsE'), 'mixedcase')

    def test_numbers_in_word(self):
        self.assertEqual(camel_to_snake('num123'), 'num123')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_special_characters(self):
        self.assertEqual(camel_to_snake('sp!c@l$t^r@n&g%t#e'), 'sp!c@l$t^r@n&g%t#e')

    def test_leading_number(self):
        self.assertEqual(camel_to_snake('123start'), '123_start')

    def test_trailing_number(self):
        self.assertEqual(camel_to_snake('start123'), 'start123')

    def test_consecutive_capital_letters(self):
        self.assertEqual(camel_to_snake('ABCMN'), 'abc_mn')

    def test_consecutive_lowercase_letters(self):
        self.assertEqual(camel_to_snake('abcdEfGhI'), 'abc_def_ghi')

    def test_consecutive_capital_and_lowercase_letters(self):
        self.assertEqual(camel_to_snake('AbCDeFgHiJ'), 'abc_def_ghi_j')
