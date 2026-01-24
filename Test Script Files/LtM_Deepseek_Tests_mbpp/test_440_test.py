import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_simple_adverb(self):
        self.assertEqual(find_adverb_position("happily"), (0, 7, "happily"))

    def test_empty_string(self):
        self.assertIsNone(find_adverb_position(""))

    def test_no_adverb(self):
        self.assertIsNone(find_adverb_position("running"))

    def test_multiple_adverbs(self):
        self.assertEqual(find_adverb_position("happily running"), (0, 7, "happily"))

    def test_adverb_at_end(self):
        self.assertEqual(find_adverb_position("running happily"), (8, 15, "happily"))

    def test_adverb_with_special_characters(self):
        self.assertEqual(find_adverb_position("running@happily"), (8, 15, "happily"))
