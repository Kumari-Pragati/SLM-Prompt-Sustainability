import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_count_char_position(self):
        self.assertEqual(count_char_position("Hello, World!"), 0)
        self.assertEqual(count_char_position("Python is awesome"), 0)
        self.assertEqual(count_char_position("AaBbCc"), 3)
        self.assertEqual(count_char_position("aAaBbCc"), 3)
        self.assertEqual(count_char_position("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWxYz"), 26)
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWxYz"), 26)
        self.assertEqual(count_char_position(""), 0)
        self.assertEqual(count_char_position("a"), 0)
        self.assertEqual(count_char_position("A"), 0)
        self.assertEqual(count_char_position("aA"), 0)
        self.assertEqual(count_char_position("Aa"), 0)
