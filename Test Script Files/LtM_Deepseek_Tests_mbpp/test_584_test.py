import unittest
from mbpp_584_code import find_adverbs

class TestFindAdverbs(unittest.TestCase):

    def test_simple_adverb(self):
        self.assertEqual(find_adverbs("quickly"), "0-5: quickly")

    def test_empty_string(self):
        self.assertIsNone(find_adverbs(""))

    def test_no_adverb(self):
        self.assertIsNone(find_adverbs("This is a sentence without adverbs."))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverbs("She ran quickly and carefully."), "6-14: quickly")

    def test_adverb_at_end(self):
        self.assertEqual(find_adverbs("This is a sentence with an adverbly."), "27-32: adverbly")

    def test_adverb_at_start(self):
        self.assertEqual(find_adverbs("Quickly, act!"), "0-5: quickly")

    def test_adverb_with_special_characters(self):
        self.assertEqual(find_adverbs("It's very cleverly done!"), "6-12: very")
