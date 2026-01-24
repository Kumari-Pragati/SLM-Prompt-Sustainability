import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_adverbs(''), '')

    def test_single_adverb(self):
        self.assertEqual(find_adverbs('quickly'), '0-5: quickly')

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs('slowly and quickly'), '4-9: quickly, 13-18: slowly')

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverbs('ly quick'), '0-4: ly')

    def test_adverb_at_end(self):
        self.assertEqual(find_adverbs('quick ly'), '7-12: ly')

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverbs('quick ly slow'), '4-9: ly')

    def test_adverb_with_number(self):
        self.assertEqual(find_adverbs('thirty quickly'), '14-19: quickly')

    def test_adverb_with_punctuation(self):
        self.assertEqual(find_adverbs("It's quickly getting late."), '12-17: quickly')

    def test_adverb_with_multiple_words(self):
        self.assertEqual(find_adverbs('very quickly'), '7-12: quickly')

    def test_adverb_with_capital_letter(self):
        self.assertEqual(find_adverbs('Ly quickly'), '1-6: Ly')

    def test_adverb_with_multiple_capital_letters(self):
        self.assertEqual(find_adverbs('Ly QuicKly'), '1-8: Ly')

    def test_adverb_with_non_alphabetic_characters(self):
        self.assertEqual(find_adverbs('ly#quickly'), '')

    def test_adverb_with_non_word_characters(self):
        self.assertEqual(find_adverbs('ly-quickly'), '')

    def test_adverb_with_whitespace(self):
        self.assertEqual(find_adverbs('  ly  quickly  '), '4-9: quickly')

    def test_adverb_with_multiple_spaces(self):
        self.assertEqual(find_adverbs('  ly     quickly  '), '4-9: quickly')

    def test_adverb_with_leading_whitespace(self):
        self.assertEqual(find_adverbs('   ly quickly'), '4-9: quickly')

    def test_adverb_with_trailing_whitespace(self):
        self.assertEqual(find_adverbs('ly quickly   '), '4-9: quickly')
