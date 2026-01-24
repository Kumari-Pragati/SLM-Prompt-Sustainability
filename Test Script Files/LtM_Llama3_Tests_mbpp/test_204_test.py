import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count('hello', 'l'), 2)
        self.assertEqual(count('hello', 'h'), 1)
        self.assertEqual(count('hello', 'o'), 2)
        self.assertEqual(count('hello', 'e'), 1)
        self.assertEqual(count('hello', 'a'), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count('', 'a'), 0)
        self.assertEqual(count('a', 'a'), 1)
        self.assertEqual(count('abc', 'a'), 1)
        self.assertEqual(count('abc', 'b'), 1)
        self.assertEqual(count('abc', 'c'), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count(None, 'a')
        with self.assertRaises(TypeError):
            count('hello', None)
        with self.assertRaises(TypeError):
            count('hello', 123)
