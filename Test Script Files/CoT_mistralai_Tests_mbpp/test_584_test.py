import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(find_adverbs(''), '')

    def test_single_adverb(self):
        self.assertEqual(find_adverbs('quickly'), '0-5: quickly')

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs('slowly runs quickly'), '5-10: quickly')

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverbs('quickly runs'), '0-5: quickly')

    def test_adverb_at_end(self):
        self.assertEqual(find_adverbs('runs quickly'), '20-25: quickly')

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverbs('runs quickly jumps'), '14-19: quickly')

    def test_adverb_with_hyphen(self):
        self.assertEqual(find_adverbs('runs quickly-enough'), '20-29: quickly')

    def test_adverb_with_number(self):
        self.assertEqual(find_adverbs('runs very-quickly'), '16-26: very-quickly')

    def test_adverb_with_punctuation(self):
        self.assertEqual(find_adverbs("It's running quickly."), '12-17: quickly')

    def test_adverb_with_multiple_spaces(self):
        self.assertEqual(find_adverbs('runs very quickly   '), '16-26: quickly')

    def test_adverb_with_multiple_words(self):
        self.assertEqual(find_adverbs('runs very quickly and slowly'), '16-26: quickly')

    def test_adverb_with_capital_letter(self):
        self.assertEqual(find_adverbs('Runs very quickly'), '0-11: Runs')

    def test_adverb_with_special_characters(self):
        self.assertEqual(find_adverbs('runs!@#$%^&*very quickly'), '26-38: very')

    def test_adverb_with_multiple_special_characters(self):
        self.assertEqual(find_adverbs('runs!@#$%^&*very-quickly@#$%^&*'), '26-42: very-quickly')

    def test_adverb_with_non_alphabetic_characters(self):
        self.assertEqual(find_adverbs('runs1234ly'), '')

    def test_adverb_with_non_word_characters(self):
        self.assertEqual(find_adverbs('runs_ly'), '')
