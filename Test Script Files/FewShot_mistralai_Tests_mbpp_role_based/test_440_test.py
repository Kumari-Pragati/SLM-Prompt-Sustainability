import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_single_adverb(self):
        self.assertEqual(find_adverb_position("quickly run"), (4, 8, "ly"))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverb_position("slowly and quickly run"), (7, 13, "ly"))
        self.assertEqual(find_adverb_position("quickly and slowly run"), (10, 16, "ly"))

    def test_no_adverbs(self):
        self.assertIsNone(find_adverb_position("run"))

    def test_adverb_at_beginning(self):
        self.assertEqual(find_adverb_position("ly run"), (0, 3, "ly"))

    def test_adverb_at_end(self):
        self.assertEqual(find_adverb_position("run ly"), (9, 12, "ly"))

    def test_adverb_in_middle(self):
        self.assertEqual(find_adverb_position("run ly run"), (4, 8, "ly"))

    def test_adverb_with_hyphen(self):
        self.assertEqual(find_adverb_position("quick-ly run"), (6, 10, "ly"))

    def test_adverb_with_apostrophe(self):
        self.assertEqual(find_adverb_position("it's-ly run"), (6, 10, "ly"))
