import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_typical_use_case(self):
        text = "This is a test string with long words like Mississippi and Mississippi"
        self.assertEqual(find_long_word(text), ['Mississippi', 'Mississippi'])

    def test_edge_case_single_word(self):
        text = "Mississippi"
        self.assertEqual(find_long_word(text), ['Mississippi'])

    def test_boundary_case_short_words(self):
        text = "This is a test string with short words like mis and miss"
        self.assertEqual(find_long_word(text), [])

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            find_long_word(None)

    def test_invalid_input_no_string(self):
        with self.assertRaises(TypeError):
            find_long_word(123)
