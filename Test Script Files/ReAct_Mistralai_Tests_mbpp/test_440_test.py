import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsNone(find_adverb_position(""))

    def test_single_adverb(self):
        result = find_adverb_position("quickly")
        self.assertEqual(result, (4, 7, "ly"))

    def test_multiple_adverbs(self):
        result = find_adverb_position("slowly and quickly")
        self.assertEqual(result, (7, 13, "ly"))
        result = find_adverb_position("quickly and slowly")
        self.assertEqual(result, (14, 20, "ly"))

    def test_adverb_at_beginning(self):
        result = find_adverb_position("ly quick")
        self.assertEqual(result, (1, 3, "ly"))

    def test_adverb_at_end(self):
        result = find_adverb_position("quick ly")
        self.assertEqual(result, (6, 10, "ly"))

    def test_adverb_in_middle(self):
        result = find_adverb_position("quickly moved slowly")
        self.assertEqual(result, (11, 17, "ly"))

    def test_adverb_with_hyphen(self):
        result = find_adverb_position("well-known")
        self.assertIsNone(result)

    def test_adverb_with_apostrophe(self):
        result = find_adverb_position("it's a beautiful day")
        self.assertIsNone(result)

    def test_adverb_with_number(self):
        result = find_adverb_position("twice as fast")
        self.assertIsNone(result)
