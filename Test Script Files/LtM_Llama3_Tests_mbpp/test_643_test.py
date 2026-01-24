import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(text_match_wordz_middle("Hello world z"), 'Found a match!')

    def test_empty_input(self):
        self.assertEqual(text_match_wordz_middle(""), 'Not matched!')

    def test_no_match(self):
        self.assertEqual(text_match_wordz_middle("Hello world"), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_wordz_middle("Hello z world z"), 'Found a match!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle(123)

    def test_non_string_input2(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle([1, 2, 3])

    def test_non_string_input3(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle({"a": 1})
