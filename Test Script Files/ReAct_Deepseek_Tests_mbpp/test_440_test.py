import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):

    def test_typical_case(self):
        text = "happily"
        expected_result = (0, 7, "happily")
        self.assertEqual(find_adverb_position(text), expected_result)

    def test_no_adverb(self):
        text = "I am a sentence without adverbs"
        self.assertIsNone(find_adverb_position(text))

    def test_multiple_adverbs(self):
        text = "She ran quickly and happily"
        expected_result = (10, 17, "happily")
        self.assertEqual(find_adverb_position(text), expected_result)

    def test_adverb_at_end(self):
        text = "The end"
        self.assertIsNone(find_adverb_position(text))

    def test_empty_string(self):
        text = ""
        self.assertIsNone(find_adverb_position(text))

    def test_whitespace_only(self):
        text = " "
        self.assertIsNone(find_adverb_position(text))

    def test_adverb_at_start(self):
        text = "happily The start"
        expected_result = (0, 7, "happily")
        self.assertEqual(find_adverb_position(text), expected_result)

    def test_adverb_with_special_characters(self):
        text = "happily@!"
        expected_result = (0, 7, "happily")
        self.assertEqual(find_adverb_position(text), expected_result)
