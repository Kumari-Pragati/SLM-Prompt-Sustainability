import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match(self):
        self.assertEqual(text_match('a.*?b$'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('hello world'), 'Not matched!')

    def test_edge_case1(self):
        self.assertEqual(text_match('a.*?b'), 'Not matched!')

    def test_edge_case2(self):
        self.assertEqual(text_match('a.*?b\n'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
