import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):
    def test_simple_adverb(self):
        self.assertEqual(find_adverbs("She runs quickly."), "0-4: quickly")

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs("He speaks softly and slowly."), "7-12: slowly, 22-26: softly")

    def test_no_adverbs(self):
        self.assertEqual(find_adverbs("He walks."), "")

    def test_empty_string(self):
        self.assertEqual(find_adverbs(""), "")

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverbs("Only quickly, she runs."), "0-5: quickly")

    def test_adverb_at_end(self):
        self.assertEqual(find_adverbs("She runs quickly, and that's all."), "40-44: all")

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverbs("She runs quickly, but not slowly."), "13-17: slowly")

    def test_adverb_with_hyphen(self):
        self.assertEqual(find_adverbs("She runs very-quickly."), "13-20: very-quickly")

    def test_adverb_with_apostrophe(self):
        self.assertEqual(find_adverbs("She runs 'very' quickly."), "24-31: very")
