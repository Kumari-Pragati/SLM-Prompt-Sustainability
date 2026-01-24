import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):

    def test_count_charac(self):
        self.assertEqual(count_charac("Hello"), 5)
        self.assertEqual(count_charac(""), 0)
        self.assertEqual(count_charac("a"), 1)
        self.assertEqual(count_charac("abc"), 3)
        self.assertEqual(count_charac("123"), 3)
        self.assertEqual(count_charac("Hello World"), 11)
