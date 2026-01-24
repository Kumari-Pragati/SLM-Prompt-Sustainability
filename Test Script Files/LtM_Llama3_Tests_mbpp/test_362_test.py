import unittest
from mbpp_362_code import max_occurrences

class TestMaxOccurrences(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_occurrences([1, 2, 3, 2, 1]), 2)
        self.assertEqual(max_occurrences([5, 5, 5, 5, 5]), 5)
        self.assertEqual(max_occurrences([1, 2, 3, 4, 5]), 1)

    def test_edge(self):
        self.assertEqual(max_occurrences([]), None)
        self.assertEqual(max_occurrences([1]), 1)
        self.assertEqual(max_occurrences([1, 1, 1, 1, 1]), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            max_occurrences('abc')
        with self.assertRaises(TypeError):
            max_occurrences(None)
