import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(find_adverb_position(""))

    def test_single_adverb(self):
        self.assertEqual(find_adverb_position("quickly"), (4, 7, "ly"))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverb_position("slowly and quickly"), (7, 13, "ly"))
        self.assertEqual(find_adverb_position("quickly and slowly"), (11, 17, "ly"))

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverb_position("ly running"), (1, 4, "ly"))

    def test_adverb_at_end(self):
        self.assertEqual(find_adverb_position("running ly"), (6, 10, "ly"))

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverb_position("running quickly"), (11, 16, "ly"))

    def test_adverb_with_hyphen(self):
        self.assertEqual(find_adverb_position("well-known"), None)

    def test_adverb_with_apostrophe(self):
        self.assertEqual(find_adverb_position("it's raining"), None)
