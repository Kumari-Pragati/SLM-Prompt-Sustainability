import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_count_function(self):
        self.assertEqual(count('hello', 'l'), 2)
        self.assertEqual(count('hello', 'o'), 1)
        self.assertEqual(count('hello', 'h'), 1)
        self.assertEqual(count('hello', 'e'), 1)
        self.assertEqual(count('hello', 'b'), 0)
        self.assertEqual(count('', 'a'), 0)
        self.assertEqual(count('abc', 'a'), 1)
        self.assertEqual(count('abc', 'b'), 1)
        self.assertEqual(count('abc', 'c'), 1)
        self.assertEqual(count('abc', 'd'), 0)

    def test_count_function_edge_cases(self):
        self.assertEqual(count('a', 'a'), 1)
        self.assertEqual(count('a', 'b'), 0)
        self.assertEqual(count('a', ''), 0)
        self.assertEqual(count('', ''), 0)
        self.assertEqual(count('a', None), 0)
