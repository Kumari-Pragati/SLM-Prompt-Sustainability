import unittest
from mbpp_684_code import count_Char

class TestCount_Char(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_Char('hello', 'o'), 2)
        self.assertEqual(count_Char('world', 'o'), 0)
        self.assertEqual(count_Char('abc', 'a'), 1)
        self.assertEqual(count_Char('xyz', 'z'), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Char('', 'a'), 0)
        self.assertEqual(count_Char('a', 'a'), 1)
        self.assertEqual(count_Char('a' * 100, 'a'), 100)
        self.assertEqual(count_Char('a' * 1000, 'a'), 1000)

    def test_complex_and_corner_cases(self):
        self.assertEqual(count_Char('hello world', 'o'), 2)
        self.assertEqual(count_Char('hello world', 'l'), 3)
        self.assertEqual(count_Char('hello world', 'd'), 1)
