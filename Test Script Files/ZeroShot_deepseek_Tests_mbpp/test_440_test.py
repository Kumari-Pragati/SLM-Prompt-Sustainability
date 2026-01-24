import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_adverb_at_start(self):
        self.assertEqual(find_adverb_position("happily ever after"), (0, 8, "happily"))

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverb_position("to boldly go where no one has gone before"), (20, 30, "where"))

    def test_adverb_at_end(self):
        self.assertEqual(find_adverb_position("I am not afraid of death, I fear life without you"), (52, 60, "without"))

    def test_no_adverb(self):
        self.assertIsNone(find_adverb_position("I am a sentence without adverbs"))

    def test_adverb_with_punctuation(self):
        self.assertEqual(find_adverb_position("Let's go swimmingly!"), (10, 20, "swimmingly"))
