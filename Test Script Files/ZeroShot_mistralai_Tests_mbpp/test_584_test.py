import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(find_adverbs(''), '')

    def test_single_word(self):
        self.assertEqual(find_adverbs('quick'), '')
        self.assertEqual(find_adverbs('happy'), '')
        self.assertEqual(find_adverbs('slow'), '')

    def test_single_adverb(self):
        self.assertEqual(find_adverbs('quickly'), '0-5: quickly')
        self.assertEqual(find_adverbs('happily'), '9-15: happily')
        self.assertEqual(find_adverbs('slowly'), '12-18: slowly')

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs('quickly and slowly'), '0-5: quickly, 12-18: slowly')
        self.assertEqual(find_adverbs('happily and quickly'), '9-15: happily, 0-4: quickly')
        self.assertEqual(find_adverbs('slowly and happily'), '12-18: slowly, 9-16: happily')

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverbs('ly quick'), '0-1: ly')
        self.assertEqual(find_adverbs('ly happy'), '0-2: ly')
        self.assertEqual(find_adverbs('ly slowly'), '0-2: ly')

    def test_adverb_at_end(self):
        self.assertEqual(find_adverbs('quick ly'), '5-6: ly')
        self.assertEqual(find_adverbs('happy ly'), '9-10: ly')
        self.assertEqual(find_adverbs('slow ly'), '12-13: ly')

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverbs('quickly happy'), '0-5: quickly, 9-10: happy')
        self.assertEqual(find_adverbs('happy quickly'), '9-10: happy, 0-5: quickly')
        self.assertEqual(find_adverbs('slowly happy'), '12-13: slowly, 9-10: happy')
        self.assertEqual(find_adverbs('happy slowly'), '9-10: happy, 12-13: slowly')
