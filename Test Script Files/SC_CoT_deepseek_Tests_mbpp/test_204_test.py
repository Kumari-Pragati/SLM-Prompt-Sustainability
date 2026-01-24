import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count('abc', 'b'), 1)
        self.assertEqual(count('aaaa', 'a'), 4)
        self.assertEqual(count('hello', 'l'), 2)

    def test_edge_case(self):
        self.assertEqual(count('', 'a'), 0)
        self.assertEqual(count('a', ''), 0)
        self.assertEqual(count('', ''), 0)

    def test_corner_case(self):
        self.assertEqual(count('abc', 'd'), 0)
        self.assertEqual(count('aaaa', 'b'), 0)
        self.assertEqual(count('hello', ' '), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count(123, 'a')
        with self.assertRaises(TypeError):
            count('abc', 123)
