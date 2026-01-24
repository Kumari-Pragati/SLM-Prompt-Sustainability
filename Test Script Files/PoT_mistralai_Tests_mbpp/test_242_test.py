import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_charac("hello"), 5)
        self.assertEqual(count_charac("Python"), 6)

    def test_edge_case_empty_string(self):
        self.assertEqual(count_charac(""), 0)

    def test_edge_case_single_character(self):
        self.assertEqual(count_charac("a"), 1)

    def test_edge_case_whitespace(self):
        self.assertEqual(count_charac(" "), 1)

    def test_corner_case_unicode(self):
        self.assertEqual(count_charac("\u03a9"), 1)
