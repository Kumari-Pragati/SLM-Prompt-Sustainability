import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum(1, 1), 0)
        self.assertEqual(sum(2, 2), 0)
        self.assertEqual(sum(3, 3), 0)
        self.assertEqual(sum(4, 4), 0)
        self.assertEqual(sum(5, 5), 0)

    def test_edge(self):
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(0, 1), 0)
        self.assertEqual(sum(1, 0), 0)
        self.assertEqual(sum(1, 2), 1)
        self.assertEqual(sum(2, 1), 1)

    def test_max(self):
        self.assertEqual(sum(100, 100), 0)
        self.assertEqual(sum(100, 101), 1)
        self.assertEqual(sum(101, 100), 1)

    def test_min(self):
        self.assertEqual(sum(-1, -1), 0)
        self.assertEqual(sum(-1, 0), 0)
        self.assertEqual(sum(0, -1), 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            sum('a', 1)
        with self.assertRaises(TypeError):
            sum(1, 'b')
