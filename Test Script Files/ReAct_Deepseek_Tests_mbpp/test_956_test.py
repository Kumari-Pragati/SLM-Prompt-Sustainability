import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_list('AtypicalCase'), ['AtypicalCase'])

    def test_multiple_words(self):
        self.assertEqual(split_list('AtypicalCaseAnotherCase'), ['AtypicalCase', 'AnotherCase'])

    def test_capital_letter_only(self):
        self.assertEqual(split_list('ABC'), ['ABC'])

    def test_no_capital_letter(self):
        self.assertEqual(split_list('typicalcase'), [])

    def test_empty_string(self):
        self.assertEqual(split_list(''), [])

    def test_mixed_case(self):
        self.assertEqual(split_list('AtypicalCaseAnotherCase123'), ['AtypicalCase', 'AnotherCase123'])

    def test_capital_letter_at_end(self):
        self.assertEqual(split_list('typicalcaseA'), ['typicalcaseA'])

    def test_capital_letter_at_start(self):
        self.assertEqual(split_list('ATypicalCase'), ['ATypicalCase'])

    def test_capital_letter_in_middle(self):
        self.assertEqual(split_list('typicalCaseAnotherCase'), ['typicalCase', 'AnotherCase'])

    def test_capital_letter_with_special_chars(self):
        self.assertEqual(split_list('Atypical!Case'), ['Atypical!Case'])

    def test_capital_letter_with_numbers(self):
        self.assertEqual(split_list('A1typicalCase'), ['A1typicalCase'])
