import unittest
from mbpp_242_code import count_charac

class TestCountCharac(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(count_charac("hello"), 5)
        self.assertEqual(count_charac("world"), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_charac(""), 0)
        self.assertEqual(count_charac("a" * 10000), 10000)
        self.assertEqual(count_charac("\t"), 1)
        self.assertEqual(count_charac("\n"), 1)

    def test_complex_input(self):
        self.assertEqual(count_charac("hello, world!"), 12)
        self.assertEqual(count_charac("HellO wOrLd!"), 12)
        self.assertEqual(count_charac("HellO wOrLd!123"), 15)
