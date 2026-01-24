import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 1), 1)

    def test_edge(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 0), 0)

    def test_edge2(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 5), 0)

    def test_edge3(self):
        self.assertEqual(removals([1, 2, 3, 4, 5], 5, 6), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            removals([], 0, 1)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            removals([1, 2, 3, 4, 5], 'a', 1)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            removals([1, 2, 3, 4, 5], 5, 'a')
