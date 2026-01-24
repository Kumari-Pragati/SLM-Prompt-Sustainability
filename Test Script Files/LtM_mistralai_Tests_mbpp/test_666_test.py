import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_char("hello", "l"), 3)
        self.assertEqual(count_char("Python", "t"), 1)
        self.assertEqual(count_char("12345", "5"), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(count_char("", "a"), 0)
        self.assertEqual(count_char("abc", "z"), 0)
        self.assertEqual(count_char("a" * 1000, "a"), 1000)
        self.assertEqual(count_char("Python", "y"), 0)

    def test_complex_input(self):
        self.assertEqual(count_char("Python", "n"), 0)
        self.assertEqual(count_char("Python", "P"), 1)
        self.assertEqual(count_char("Python", "y" * 10), 0)
        self.assertEqual(count_char("Python", "P" * 10), 10)
