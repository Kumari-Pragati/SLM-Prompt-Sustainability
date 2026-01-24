import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_adverb_position("Quickly, he ran."), (4, 8, "ly"))
        self.assertEqual(find_adverb_position("She sings loudly."), (5, 11, "ly"))
        self.assertEqual(find_adverb_position("He walks slowly."), (6, 12, "ly"))

    def test_edge_cases(self):
        self.assertEqual(find_adverb_position(""), (0, 0, None))
        self.assertEqual(find_adverb_position("I am adverbly."), (7, 13, "ly"))
        self.assertEqual(find_adverb_position("I am adverbly, very."), (7, 13, "ly"))
        self.assertEqual(find_adverb_position("I am adverbly, very adverbly."), (7, 13, "ly"))
        self.assertEqual(find_adverb_position("I am adverbly, very adverbly, not."), (7, 13, "ly"))
