import unittest
from mbpp_440_code import find_adverb_position

class TestFindAdverbPosition(unittest.TestCase):
    def test_typical_use_case(self):
        text = "I ran quickly and slowly."
        expected_output = (14, 21, "slowly")
        self.assertEqual(find_adverb_position(text), expected_output)

    def test_multiple_adverbs(self):
        text = "I ran quickly and slowly and quietly."
        expected_output = (14, 21, "slowly")
        self.assertEqual(find_adverb_position(text), expected_output)

    def test_no_adverbs(self):
        text = "I ran."
        self.assertIsNone(find_adverb_position(text))

    def test_empty_text(self):
        text = ""
        self.assertIsNone(find_adverb_position(text))

    def test_non_string_input(self):
        text = 123
        with self.assertRaises(TypeError):
            find_adverb_position(text)
