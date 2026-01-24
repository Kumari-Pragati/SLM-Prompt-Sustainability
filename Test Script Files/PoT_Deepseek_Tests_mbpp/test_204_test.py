import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count('abcabc', 'a'), 2)
        self.assertEqual(count('hello world', 'o'), 2)

    def test_edge_case(self):
        self.assertEqual(count('', 'a'), 0)
        self.assertEqual(count('a', ''), 1)

    def test_boundary_case(self):
        self.assertEqual(count('a' * 10000, 'a'), 10000)
        self.assertEqual(count('a' * 10000, 'b'), 0)

    def test_corner_case(self):
        self.assertEqual(count('abcabc', 'abc'), 0)
        self.assertEqual(count('abcabc', 'd'), 0)
