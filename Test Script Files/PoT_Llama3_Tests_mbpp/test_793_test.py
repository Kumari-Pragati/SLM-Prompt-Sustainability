import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 3, 5), 2)
        self.assertEqual(last([10, 20, 30, 40, 50], 30, 5), 4)
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 5), 4)

    def test_edge(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 1, 5), 0)
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 5), 4)
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 0), -1)

    def test_corner(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 1, 1), 0)
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 1), 0)
        self.assertEqual(last([1, 2, 3, 4, 5], 3, 1), 0)
