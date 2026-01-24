import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count("hello", "l"), 3)
        self.assertEqual(count("Python", "t"), 1)

    def test_edge_cases(self):
        self.assertEqual(count("", "a"), 0)
        self.assertEqual(count("abc", "z"), 0)
        self.assertEqual(count("Python", "y"), 0)
        self.assertEqual(count("Python", ""), 0)
        self.assertEqual(count("Python", None), 0)

    def test_boundary_cases(self):
        self.assertEqual(count("aa", "a"), 2)
        self.assertEqual(count("Python", "P"), 1)
        self.assertEqual(count("Python", "n"), 0)
