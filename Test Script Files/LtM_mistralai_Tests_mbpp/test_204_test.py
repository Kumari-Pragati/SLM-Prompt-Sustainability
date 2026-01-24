import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count("hello", "l"), 3)
        self.assertEqual(count("Python", "t"), 1)
        self.assertEqual(count("1234", "4"), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count("", "a"), 0)
        self.assertEqual(count("abcdefghijklmnopqrstuvwxyz", "z"), 1)
        self.assertEqual(count("A" * 100, "A"), 100)
        self.assertEqual(count("", ""), 0)

    def test_complex_scenarios(self):
        self.assertEqual(count("Python", "y"), 0)
        self.assertEqual(count("Python", "P"), 1)
        self.assertEqual(count("Python", "p"), 1)
        self.assertEqual(count("Python", "Q"), 0)
